from collections import defaultdict
from pathlib import Path
import os
import re
import string
import random
import shutil 
import csv
from datetime import datetime




ORIGINAL_IN_DIR = Path(os.path.join(Path.cwd(),"..","quartz","raw"))
IN_DIR = Path(os.path.join(Path.cwd(),"..","quartz","raw_copy"))
OUT_DIR = Path(os.path.join(Path.cwd(),"..","quartz","content"))
DEFAULT_DRAFT = False
TIMESTAMP_FILE = "./timestamp.csv"
TIMESTAMP_HEADER = ["Name","Date"]

# --- CHANGE THE ABOVE, NOTHING BELOW THIS LINE ---



def sanitize_string(s):
    """
    given some string s, make it url-friendly
    """
    # replace spaces with -'s and remove all other url unfriendly chars
    s = re.sub(' ', '-', s)
    s = re.sub('[^0-9a-zA-Z\-\._~]', '', s)
    # dedupe -'s
    s = re.sub('-+', '-', s)
    return s.lower()

def sanitize_link(link, files, verbose=True):
    """
    given some Wikilink in the form [[FILENAME#HEADER|VISIBLE]],
    translate to Markdown Link in the form [VISIBLE](FILENAME#HEADER)
    """
    if verbose:
        print(f'Sanitizling link {link}')
    brace = link.find(']')
    pound = link.find('#')
    pipe = link.find('|')
    end_index = min([elt for elt in [brace, pound, pipe] if elt != -1])
    open_brace_index = 2
    filename_portion = link[open_brace_index:end_index]
    visible_portion = filename_portion
    if pipe != -1:
        visible_portion = link[pipe+1:brace]
    header = ''
    if pound != -1:
        if pipe != -1:
            header = link[pound:pipe]
        else:
            header = link[pound:brace]

    # get relative filepath
    search_filename = sanitize_string(filename_portion)
    rel_link = None
    for file in files:
        if search_filename == file.stem:
            rel_link = file.relative_to(OUT_DIR.parent)
    if rel_link:
        rel_link = rel_link.relative_to(*rel_link.parts[:1])
    # build Markdown link from Wikilink components and make all backslashes forward slashes
    sanitized_link = f'[{visible_portion}]' + f'({rel_link}{header})'
    sanitized_link = re.sub('\\\\', '/', sanitized_link)
    return sanitized_link

def escape_re_special_characters(s):
    """
    given some string,
    return a regex that matches that string literal
    """
    for re_special_char in '/\-[]{}()*+?.,^$|#':
        s = re.sub(f'\{re_special_char}', f'\{re_special_char}', s)
    return s

def add_frontmatter(s, title, default_draft=DEFAULT_DRAFT):
    """
    given some note body s and title of note title,
    return the note body with frontmatter appended

    if default_draft, makes all notes drafts
    """
    lines = s.split('\n')
    # if there is no existent frontmatter
    if not lines[0].startswith('---'):
        if default_draft:
            new_lines = f"""---
title: {title}
draft: true
---""".split('\n') + lines
        else:
            new_lines = f"""---
title: {title}
---""".split('\n') + lines
    else:
        if default_draft:
            lines.insert(1, 'draft: true')

        has_title = False
        for i, line in enumerate(lines):
            # make all urls tags 'website' tags to make Hugo-compliant
            if line.startswith('url:'):
                lines[i] = line.replace('url: ', 'website: ')
            # take all colons out of titles to make Hugo-compliant
            if line.startswith('title:'):
                has_title = True
                lines[i] = 'title: ' + line.replace('title: ', '').replace(':', '').replace("'", '')
        if not has_title:
            lines.insert(1, f'title: {title}')

        new_lines = lines
    return '\n'.join(new_lines)

def sanitize_file_contents(path, files):
    """
    given the path to a note and a list of all Obsidian files,
    edits the note body to make Quartz-compliant
    """
    with open(str(path), "r", encoding='utf-8') as f:
        old_text = f.read()

    with open(str(path), "w", encoding='utf-8') as f:
        links = re.findall('\[\[[^\]]*\]\]', old_text)
        sanitized_text = old_text
        for link in links:
            sanitized_link = sanitize_link(link, files)
            escaped_special_chars_link = escape_re_special_characters(link)
            sanitized_text = re.sub(escaped_special_chars_link, sanitized_link, sanitized_text)

        f.write(sanitized_text)

def sanitize_file_name(path):
    """
    given the path to a note,
    copies the note to the OUT_DIR
    and makes filename Quartz-compliant

    note that two non-colliding notes '@this' and 'this'
    will have url-unfriendly chars such as '@' removed, making them collide.
    in this case one will have a random string appended to its filename to avoid collision
    """
    sanitized_parents = [sanitize_string(str(p.stem)) for p in path.relative_to(IN_DIR).parents]
    sanitized_relpath = OUT_DIR
    for p in sanitized_parents[::-1]:
        sanitized_relpath = sanitized_relpath/p
    new_file_path = sanitized_relpath/(sanitize_string(path.stem) + '.md')
    os.makedirs(new_file_path.parent, exist_ok=True)

    # make sure no two notes collide
    if os.path.isfile(new_file_path):
        new_file_path = new_file_path.parent/(''.join(random.choice(string.ascii_lowercase) for i in range(10)) + new_file_path.suffix)

    with open(str(new_file_path), "w", encoding='utf-8') as f:
        with open(str(path), "r", encoding='utf-8') as f_old:
            old_text = f_old.read()

        frontmattered_text = add_frontmatter(old_text, path.stem)
        f.write(frontmattered_text)

def copy_and_overwrite(from_path, to_path):
    if os.path.exists(to_path):
        shutil.rmtree(to_path)
    shutil.copytree(from_path, to_path)


if __name__ == '__main__':
    # First copy the obsidian
    copy_and_overwrite(ORIGINAL_IN_DIR,IN_DIR)
    if os.path.exists(OUT_DIR):
        shutil.rmtree(OUT_DIR)
    
    os.makedirs(OUT_DIR)
    os.makedirs(os.path.join(OUT_DIR,"notes"))
    highlights = os.listdir(os.path.join(IN_DIR,"highlights"))
    highlights_path = os.path.join(OUT_DIR,"notes","highlights.md")

    if os.path.exists(highlights_path):
        os.remove(highlights_path)
    
    existing_data = {}
    new_data = {}
    with open(TIMESTAMP_FILE,'r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        for index,row in enumerate(csv_reader):
            if index == 0:
                continue
            name,date = row
            
            formatted_date = datetime.strptime(date, '%d-%m-%Y')
            
            existing_data[name] = formatted_date
    
    if len(existing_data) == 0:
        with open(TIMESTAMP_FILE,'w') as file:
            writer = csv.writer(file)
            writer.writerow(TIMESTAMP_HEADER)
    
        
    for highlight in highlights:
        if highlight not in existing_data:
            formatted_date = datetime.today()
            existing_data[highlight] = formatted_date
            new_data[highlight] = formatted_date


    files = [f for f in IN_DIR.rglob("*") if Path(f).suffix == '.md']
    
    sorted_highlights = [(highlight,existing_data[highlight]) for highlight in highlights]
    sorted_highlights = sorted(sorted_highlights,key = lambda x : x[1])
    
    #We now do a count per month
    counts = defaultdict(int)
    for highlight in sorted_highlights:
        date = highlight[1]
        counts[f'01-{date.strftime("%m-%Y")}']+=1
    


    with open(highlights_path,"w") as file:
        file.write("---\ntitle: Reading Highlights\n---\nA list of the {} Articles I've read so far\n\n".format(len(highlights)))

        file.write("# Some Stats")
        months = sorted(counts.keys())

        if months:
            file.write("\n\n|Period|Amount Read|\n|----|----|\n")

        for month in months:
            key = datetime.strptime(month, '%d-%m-%Y').strftime("%B %Y")
            file.write(f'|{key}|{counts[month]}|\n')


        file.write("\n\n # Articles\n")
        for highlight,date in sorted_highlights:
            formatted_date = date.strftime('%d-%m-%Y')
            fileLink = f'- [{highlight[:-3]}](highlights/{sanitize_string(highlight)})\n'
            file.write(fileLink)
        file.close()
    

    
    
    for file in files:
        sanitize_file_name(file)
    
    
    # We read in highlights folder
    with open(TIMESTAMP_FILE,"a+") as file:
        writer = csv.writer(file)
        for highlight in new_data.keys():
            formatted_date =  new_data[highlight].strftime('%d-%m-%Y')
            writer.writerow([highlight,formatted_date])


    renamed_files = [f for f in OUT_DIR.rglob("*") if Path(f).suffix == '.md']
    for file in renamed_files:
        sanitize_file_contents(file, renamed_files)
