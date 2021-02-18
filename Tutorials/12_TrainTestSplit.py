# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 20:08:42 2021

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

# Define X and Y

X = df[["carat", "x", "y", "z"]]
y = df["price"]

#%% Train-Test-Split

# Load Train-Test_split

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size= 0.75,
                                                    random_state= 50)

#%% Scikit-Learn LinearRegression

# Load the LinearRegression
from sklearn.linear_model import LinearRegression

# Save the model into a variable
model = LinearRegression()

# Fit the model
model.fit(X_train, y_train)

# Score
print(model.score(X_test, y_test)) # R2 on test data!





