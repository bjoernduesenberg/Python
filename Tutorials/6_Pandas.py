# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 09:30:29 2021

@author: Björn Düsenberg
"""

#%% Pandas - seperator ","

import pandas as pd

path = "path..."
df = pd.read_csv(path + "teilnehmer.csv")

print(df.head())

#%% Pandas - seperator ";"

path = "path..."
df = pd.read_csv(path + "teilnehmer-semikolon.csv", sep=";") # Seperator definieren

print(df.head())

#%% Pandas - seperator "\t"

path = "path..."
df = pd.read_csv(path + "teilnehmer.tsv", sep="\t") # Seperator definieren

print(df.head())

#%% 

path = "path..."
df = pd.read_csv(path + "GlobalLandTemperaturesByMajorCity.csv.bz2")

print(df.head())

#%% Nützliche Pandas Befehle
 
# print(df.columns) # Liste all columns
# print(df.head(x)) # Print the first x rows
# print(len(df)) # Length of the data frame
# print(df["Y"]) # Pandas series of column "Y"
# print(df.info()) # Some details
# print(df.describe()) # Some statistical key values
# print(df.describe(include = "all")) # statistical key values of all columns
# print(df.tail(x)) # Print th elast x rows

#%% Access to data frame

# Columns
print(df["City"]) # Pandas series column "City"
print(df["City"][1000:1010]) # Pandas series column "City" entries 1000:1010
print(df[["Country", "City"]]) # Access to several columns --> Lists as input are possible
print(df[["Country", "City"]].head()) # .head() function for first rows

#%% Delete
# Delete column
df_2 = df.drop(["AverageTemperatureUncertainty"], axis = 1) # Save into new DF
df.drop(["AverageTemperatureUncertainty"], axis = 1, inplace = True) # Save into original DF

# Delete row
df_3 = df.drop([1])

#%% Calculations within a row

print(df["AverageTemperature"].mean()) # Mean
print(df["AverageTemperature"].max()) # Maximum
print(df["AverageTemperature"].min()) # Minimum
print(df["AverageTemperature"].sum()) # Sum
print(df["AverageTemperature"].to_numpy()) # To numpy array
 #%% Plotting directly from Pandas with Matplotlib
 
%matplotlib qt

import matplotlib as plt
df["AverageTemperature"].plot.hist()

#%% Access to rows 1.1

# .loc function

path = "path..."
df = pd.read_csv(path + "GlobalLandTemperaturesByMajorCity.csv.bz2")

print(df.loc[0]) # Access to row [0]
a = dict(df.loc[0]) # Save as dictionary

print(df["City"].loc[10000]) # Column "City" row 10000

#%% Access to rows 1.2

# Filter
print(df["Country"] == "Germany") # --> Query creates series with True/False values

df_germany = df[df["Country"] == "Germany"] # --> Filter "Country" == "Germany" 
print(df_germany.head())

print(df_germany.iloc[0]) # Acess row [0]

#%% Change Dataframe

df["Country"] = "World" # Set all entries from column "Country" to "World
df["Planet"] = "World" # Create a new column "Planet" and set all entries from the "Country" column to "World".

df["AverageTemperatureNew"] = df["AverageTemperatureNew"] + 5 # Take all entries from a column and add 5

#  .loc is able to filter columns
# Access to all rows in "Country" == "Germany", Show "Country"
df.loc[df["Country"] == "Germany", "Country"]

# Results can direclty be changed
df.loc[df["Country"] == "Germany", "Country"] = "Deutschland"










