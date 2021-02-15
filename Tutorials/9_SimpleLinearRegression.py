# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 17:29:43 2021

@author: Björn Düsenberg
"""

#%% Import Modules

# Basic modules
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
import seaborn as sns

#%% Numpy repitition

# Reshape 
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(a.reshape(-1 , 1))

# Each column is a "feature" within the machine learning world
# --> The amount of features is important

#%% Linear regression

# Load data
df = pd.read_csv("data/Diamonds/diamonds.csv.bz2")

print(df.head())

#%% Plot a sample

sns.scatterplot(data = df.sample(100),
                x = "carat",
                y = "price")

#%% Set X and Y 

#X = df[["carat"]] 
X = df["carat"].to_numpy().reshape(-1 , 1)

#Y = df[["price"]]
y = df["price"].to_numpy()

#%% Scikit - Learn module

# Load the LinearRegression
from sklearn.linear_model import LinearRegression

# Save the model into a variable
model = LinearRegression()

# Fit the model
model.fit(X, y)

#%% Access to model parameters - Coefficient and intercept

print(model.coef_)
print(model.intercept_)

# y = m * x + b
# price = 7756.42561797 * {weight in carat} - 2256.36058005

#%% Calculate the price with a function

# Use the coefficient and intercept within a self written function

def get_price(carat):
    return 7756.42561797 * carat -2256.36058005

print(get_price(1))

#%% Predict

# Prediction of one or several values
# model.predict(np.array[[...]])

print(model.predict([
    [1],
    [2],
    [10]
    ]))

#%% Plot of the linear regression

x_pred = np.array([3, 0])
y_pred = model.predict(x_pred.reshape(-1, 1))

sns.lineplot(x_pred, y_pred, color = "red")
sns.scatterplot(x = "carat", y = "price", data = df.sample(50))





















































