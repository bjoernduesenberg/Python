# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 19:51:05 2021

@author: Björn Düsenberg
"""

#%% Import Modules

# Basic modules
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns

#%% Data

# Load data
df = pd.read_csv("data/Diamonds/diamonds.csv.bz2")

print(df.head())

#%% Set X and Y 

X = df["carat"].to_numpy().reshape(-1 , 1)
y = df["price"].to_numpy()

#%% Scikit-Learn LinearRegression

# Load the LinearRegression
from sklearn.linear_model import LinearRegression

# Save the model into a variable
model = LinearRegression()

# Fit the model
model.fit(X, y)

#%% Access to model parameters - Coefficient and intercept

print(model.coef_)
print(model.intercept_)

#%% R2 - Score

# Load r2_score
from sklearn.metrics import r2_score

# Array with predicted prices
y_pred = model.predict(X)

print(r2_score(y, y_pred))
# --> ~ 0.85

#%% Alternative R2 - score from the model!

# Use of the X and y values from the training
print(model.score(X, y))
# --> ~ 0.85

#%% Compare models

# Save the model into a variable
model_2 = LinearRegression()

# Define X / Y
X_train = df[["carat", "x", "y", "z"]] # weight in carat and dimensions x, y, z
y_train = df[["price"]] # Array

#Fit
model_2.fit(X_train, y_train)

print(model_2.score(X_train, y_train))
# --> 0.854 - slightly higher




























