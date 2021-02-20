# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 06:40:16 2021

@author: Björn Düsenberg
"""

#%% Import Modules

# Basic modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#%% Import Data

# Load data
df = pd.read_csv("data/Autos/autos.csv.bz2", encoding = "iso-8859-1")

print(df.columns)

#%% pre - Filter 

df = df[df["offerType"] == "Angebot"]
df = df[df["vehicleType"] == "kleinwagen"]
df = df[df["notRepairedDamage"] == "nein"]

df.dropna(inplace = True)

#%% One Hot encoding

# Load packages from sklearn
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

# Define X and y
X = df[["kilometer", "yearOfRegistration", 'brand', "gearbox", "fuelType"]]
y = df["price"]

# Create ColumnTransformer
cf = ColumnTransformer([
    ("brand", OneHotEncoder(), ["brand", "gearbox", "fuelType"]) # (New name, OneHotEncoder(), ["ColumnsToEncode"])
    ], remainder = "passthrough") 

cf.fit(X) # Use cf on X
print(cf.transform(X).toarray()) # Show the transformation of the dataframe

X_trans = cf.transform(X).toarray() # Transform and save - .toarray !!! shape is important

#%% Train-Test-Split

# Load Train-Test_split

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X_trans, y, train_size= 0.75,
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

#%% Categorical features

# One-Hot-Encoding










