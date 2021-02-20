# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 09:11:41 2021

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
df = pd.read_csv("data/Diabetes/diabetes.csv")

print(df.columns)

#%% Logistic Regression

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

X = df[["BMI", "Age", "BloodPressure", "Glucose"]]
y = df["Outcome"] # Single parentesis 

X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    train_size= 0.75,
                                                    random_state=50)

model = LogisticRegression()
model.fit(X_train, y_train)

# print(model.score(X_test, y_test))

#%% Confusion matrix

from sklearn.metrics import confusion_matrix

y_pred = model.predict(X_test)

print(confusion_matrix(y_test, y_pred))

#%% Plot CM

from sklearn.metrics import plot_confusion_matrix

plot_confusion_matrix(model, X_test, y_test, normalize = "all")












