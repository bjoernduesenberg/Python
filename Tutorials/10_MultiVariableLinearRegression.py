# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 19:35:39 2021

@author: Björn Düsenberg
"""

#%% Import Modules

# Basic modules
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns

#%% Multivariable linear regression

# Load data
df = pd.read_csv("data/Diamonds/diamonds.csv.bz2")

# Load the LinearRegression
from sklearn.linear_model import LinearRegression

# Save the model into a variable
model = LinearRegression()

# Define X / Y

X_train = df[["carat", "x", "y", "z"]] # weight in carat and dimensions x, y, z
y_train = df[["price"]] # Array

# Fit the model
model.fit(X_train, y_train)

#%% Coefficient and intercept

print(model.coef_)
print(model.intercept_)

#%% Use the model - predict 3 Diamonds

X_test = np.array([
    [2, 5, 2, 6], # Diamond 1
    [0.5, 4, 2, 5], # Diamond 2
    [0.5, 3, 2, 4], # Diamond 3
    ])

print(model.predict(X_test))