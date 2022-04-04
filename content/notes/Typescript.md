---
title: Typescipt
---

# Overview
> Typescript is an open source, typed syntactic superset of Javascript. It compiles to readable JS

Using typescript, we can write better programs which are easier to edit and refactor down the line.

A good way to think of TS files:

-   `.ts` files contain both type information and code that runs
-   `.js` files contain only code that runs
-   `.d.ts` files contain only type information

# Cookbook

**Functions**

We can annote types by

```
function add(a : number, b:number):number {
  return a + b 
}
```

**Objects**

