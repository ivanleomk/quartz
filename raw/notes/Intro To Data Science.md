---
title: "Intro To Data Science"
last-updated: "2022-04-24"
---

# Linear Regression

```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error

model = LinearRegression()

# Create the design matrix X and the target vector y
y = data['mpg']
X = data.drop(columns=['mpg'])

# Fit the model (notice no normal equations!)
model.fit(X, y)

# Make predictions using the model
model.predict(X)[:10]

# Get Model Coeffecients
model.coef_

# Get Model Intercepts
model.intercept_

Yhat = predict(data[["X0", "X1"]].to_numpy()).flatten()
    # Compute and print error metrics
print("Mean Absolute Error:", mean_absolute_error(Y, Yhat))
print("Root Mean Squared Error:", np.sqrt(mean_squared_error(Y, Yhat)))
```

# Missing Values
```python
from seaborn import load_dataset
data = load_dataset("mpg")



# We can use DataFrame.isna to find rows with missing values
data[data.isna().any(axis=1)]

# We then use a feature to indicate that the value was missing
def phi_cont(df):
    Phi = df[["cylinders", "displacement", 
              "horsepower", "weight", 
              "acceleration", 
              "model_year"]].copy()
    Phi["horsepower_missing"] = Phi["horsepower"].isna()
    Phi = Phi.fillna(Phi.mean())
    return Phi


model = LinearRegression()
model.fit(phi_cont(data), data[["mpg"]])
```


# Plotting Functions
## Keeping Track of Models
```python
def evaluate_model(name, model, phi, models=dict()):
    # run the prediction function and compute the RMSE
    Yhat = model.predict(phi(data)).flatten()
    Y = data['mpg'].to_numpy()
    rmse = np.sqrt(mean_squared_error(Y, Yhat))
    print("Root Mean Squared Error:", rmse)
    
    # Save the model and rmse to the collection of models 
    models[name] = dict(model=model, phi=phi, rmse=rmse)
    
    # Generate diagnostic and model comparison plots
    fig = make_subplots(rows=1, cols=2)
    fig.add_trace(go.Scatter(x=Yhat, y=Y, mode="markers"), row=1, col=1)
    fig.update_xaxes(title = "Yhat", row=1, col=1)
    fig.update_yaxes(title = "Y", row=1, col=1)
    ymin = np.min(Yhat)
    ymax = np.max(Yhat)
    fig.add_trace(go.Scatter(x=[ymin,ymax], y=[ymin,ymax], name="y=yhat"), row=1, col=1)
    fig.add_trace(go.Bar(x=list(models.keys()), 
                         y=[models[k]['rmse'] for k in models]), row=1, col=2)    
    fig.update_layout(showlegend=False)
    fig.update_yaxes(title = "RMSE", row=1, col=2)
    fig.show()
    


models = {}

def compute_CV_error(model, X_train, Y_train):
    '''
    Split the training data into 5 subsets.
    For each subset, 
        fit a model holding out that subset
        compute the MSE on that subset (the validation set)
    You should be fitting 5 models total.
    Return the average MSE of these 5 folds.

    Args:
        model: an sklearn model with fit and predict functions 
        X_train (data_frame): Training data
        Y_train (data_frame): Label 

    Return:
        the average validation MSE for the 5 splits.
    '''
    # Define a KFold object with 5 splits
    kf = KFold(n_splits = 5, random_state = 42, shuffle = True)
    validation_errors = []
    
    for train_idx, valid_idx in kf.split(X_train):
        # split the data
        split_X_train, split_X_valid = X_train.iloc[train_idx, :], X_train.iloc[valid_idx, :]
        split_Y_train, split_Y_valid = Y_train.iloc[train_idx], Y_train.iloc[valid_idx]

        # Fit the model on the training split
        model.fit(split_X_train,split_Y_train)
        
        # Compute the RMSE on the validation split
        error = rmse(split_Y_valid, model.predict(split_X_valid))

        validation_errors.append(error)
        
    return np.mean(validation_errors)

compute_CV_error(lm.LinearRegression(),X_train,Y_train)
```

## Using a previously computed Mean
```python
# Making a global variable
def phi_cont(df, data_mean = data.mean()):
    feature_cols = ["cylinders", "displacement", "horsepower", "weight", "acceleration", "model_year"]
    Phi = df[feature_cols].copy()
    Phi["horsepower_missing"] = Phi["horsepower"].isna().astype(float)
    Phi = Phi.fillna(data_mean)
    return Phi
```

# SKLearn Functions

### Quantative Variables
```python
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy="mean")


# We first fit the inputer to the data then we transform the data
imputer.fit(data[['weight', 'horsepower']])
imputer.transform(data[['weight', 'horsepower']])

# This makes sure that we are only transforming the specific columns we want to transform
imputer.fit(data[['horsepower']])
def phi_cont(df, imputer=imputer):
    feature_cols = ["cylinders", "displacement", "horsepower", "weight", "acceleration", "model_year"]
    Phi = df[feature_cols].copy()
    Phi["horsepower_missing"] = Phi["horsepower"].isna().astype(float)
    Phi["horsepower"] = imputer.transform(Phi[["horsepower"]]).flatten()
    return Phi
```

### Categorical Variables
```python
from sklearn.preprocessing import OneHotEncoder

# First create the object
oh_enc = OneHotEncoder()

# Then fit the object to the data
oh_enc.fit(data[['origin']])

# Then transform the data so that the data is now encoded
oh_enc.transform(data[['origin']].head())

oh_enc.get_feature_names()

# We can then utilise this in a function
def phi_with_origin(df):
    Phi = phi_with_displacement(df)
    dummies = pd.DataFrame(oh_enc.transform(df[['origin']]).todense(), 
                           columns=oh_enc.get_feature_names(),
                           index = df.index)
    return Phi.join(dummies)
```

## Text Encoding
( Lec 16 )
```python
bow = CountVectorizer()
bow.fit(data["name"])

def phi_with_name(df):
    Phi = phi_with_origin(df)
    bow_encoding = pd.DataFrame(
        bow.transform(df['name']).todense(), 
        columns=bow.get_feature_names(),
        index = df.index)
    return Phi.join(bow_encoding)
```

## Hot Encoding
```python
one_hot_encoded_NO2 = NO2.join(pd.get_dummies(NO2["hour_of_day"], drop_first=True)).drop("hour_of_day", axis=1)
one_hot_encoded_NO2.head(5)
```
# Cross Validation

```python
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.base import clone

from seaborn import load_dataset
data = load_dataset("mpg")
data

# We delete rows don't have missing data
data = data[~data.isna().any(axis=1)].copy()

tr, te = train_test_split(data, test_size = 0.1,random_state=83)



def cross_validate_rmse(phi_function, model):
    model = clone(model)
    five_fold = KFold(n_splits = 5, random_state = 100, shuffle = True)
    rmse_values = []
    for tr_ind, va_ind in five_fold.split(tr):
        
        X_train = phi_function(tr.iloc[tr_ind, :])
        y_train = tr['mpg'].iloc[tr_ind]
        X_val = phi_function(tr.iloc[va_ind, :])
        y_val = tr['mpg'].iloc[va_ind]
        
        model.fit(X_train, y_train)
        
        rmse_values.append(rmse(y_val, model.predict(X_val)))
        
    return np.mean(rmse_values)



```

# Logistical Regression
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objs as go
from scipy.optimize import minimize
import sklearn.linear_model as lm

# Configuring Params
plt.rcParams['figure.dpi'] = 150
plt.rcParams['lines.linewidth'] = 3
sns.set()


# Reading Data
df = pd.read_csv('nba.csv')

# Encoding the result using a binary 1 0 variable
df["WON"] = df["WL"]
df["WON"] = df["WON"].replace("W", 1)
df["WON"] = df["WON"].replace("L", 0)



```

# K-Means

```python
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import random
from sklearn.cluster import KMeans

# Import Data
iris = pd.read_csv("iris.csv")
iris.sample(10)

# Visualize data
sns.scatterplot(data = iris, x = "petal_length", y= "petal_width", color="black")
plt.xlabel('x')
plt.ylabel('y');

#If you need to save the figure
plt.savefig('2d_data_needing_clustering.png', dpi = 300, bbox_inches = "tight")


# Performing KMeans (Default CLusters is 8)
clustering = KMeans().fit(iris[["petal_length", "petal_width"]])

# Defining number of clusters
clustering = KMeans(n_clusters=2).fit(iris[["petal_length", "petal_width"]])


# Important Values
kmeans.cluster_centers_
kmeans.cluster_centers_

```


Hi my name is Ivan and I'm a software developer conducting a research project on consumer electronic distributors in singapore. I'm hopig to find out more about their biggest pains in hopes of creating a product to solve their biggest problems.

I don't have any products to sell and just want to ask some questions.

If you wish, I can report back to you my research findings after speaking with some other companies in the same space. It might be interesting to see where you stack up. I was just wondering if you would be willing to spend the next couple of minutes with me to be part of this process.

IF NO, I completely understand. Do you know any colleagues else who might have a couple minutes to spend with me?


Avertek
- faulty exchange
- warranty only for products
- sales@avertek.com.sg