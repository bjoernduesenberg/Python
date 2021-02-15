# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 13:35:16 2021

@author: Björn Düsenberg
"""

#%% Datentypen

import pandas as pd

path = "path..."
df = pd.read_csv(path + "GlobalLandTemperaturesByMajorCity.csv.bz2")

print(df)

#%%

print(df["AverageTemperature"]) # Type: float64
print(df["City"]) # Type: object
print(df["dt"]) # Type: object obwohl Datum

#%% NaN - Spezialwert Not a Number
# Regeln

x = float("nan")
print(x + 5) # man kann NaN in float umwandeln, wird dann als Zahl behandelt
print(x == 5) # NaN "überschreibt die Abfrage und es ist False

import math
print(math.isnan(x)) # mit dem math Modul können wir gezielt abfragen

#%% NaN in Pandas filtern
print(pd.isna(df["AverageTemperature"])) # Series mit T/F Werten 
print(~pd.isna(df["AverageTemperature"])) # Invertierte Series

# Händisch Nan aus Spalte herausfiltern
# df_isna = df[~pd.isna(df["AverageTemperature"])] # Series ohne NaN in "AverageTemperature"

# Eingebaute Pandas-Funktion - Hier für ganzes DataFrame - Löscht alle Zeilen mit NaN
print(df.dropna())

# --> Darauf achten, wie NaN repräsentiert wird - 0 kann schwierig sein

#%% Pandas und strings

# Zusammenziehen von 2 Spalten mit strings

df["City"] = df["City"] + ", " + df["Country"]
df.drop(["country"], axis = 1, inplace = True)
print(df["City"])

#%% Stringfunktionen auf Series

df["City"].str.split(", ", 1) # Splitte string am Komma 
df["City"].str.replace(",", ",,,") # Ersetze , durch ,,,

#!!!!!!!!!!!!!!!!! WICHTIG !!!!!!!!!!!!!!!!!#
df_city = df["City"].str.split(",", 1, expand = True) # Splitted und gibt DataFrame zurück

#%% Datentypen umwandeln

# Spalte "Longitude" in Float umwandeln
print(df["Longitude"])

df["Long_dir"] = df["Longitude"].str[:-1] # Erstellen einer neuen Spalte 
print(df["Long_dir"].astype("float")) # Umwandeln in float

#%% Datumswerte

print(pd.to_datetime("2019-05-05"))
df["dt"] = pd.to_datetime(df["dt"]) # Spalte in Datumswerte umwandeln

print(df["dt"].dt.year) # Ausgabe der Jahre
print(df.loc[df["dt"].dt.year == 2012, "AverageTemperature"]) 
# Zeige alle Zeilen d. Jahres 2012
# der Spalte AverageTemperature

# Vergleich von Durchschnitsstemperaturen (Mittelwert) verschiedener Jahre
print(df.loc[df["dt"].dt.year == 2010, "AverageTemperature"].mean())
print(df.loc[df["dt"].dt.year == 2011, "AverageTemperature"].mean())
print(df.loc[df["dt"].dt.year == 2012, "AverageTemperature"].mean())
print(df.loc[df["dt"].dt.year == 2013, "AverageTemperature"].mean())

#%% Sort data

# inplace = T -> sort within the df , ascending = T 
print(df.sort_values(by = ["AverageTemperature"], inplace = True))

# Sort by several variables
print(df.sort_values(by = ["AverageTemperature", "City"], inplace = True))

#%% Group by

import numpy as np

# Group by date and summarise
# agg(new_variable = ("variable", function))
print(df.groupby(by=["dt"]).agg(
    Avgtmp=("AverageTemperature", np.mean),
    mintmp=("AverageTemperature", np.min),
    maxtmp=("AverageTemperature", np.max))
    )

#%% after year

df["dtYear"] = df["dt"].dt.year

res = df.groupby(by=["dtYear"]).agg(
    Avgtmp=("AverageTemperature", np.mean),
    mintmp=("AverageTemperature", np.min),
    maxtmp=("AverageTemperature", np.max))
    

print(res.loc[2000]) # Dataset for the year 2000
print(res.loc[1980:2000]) # Dataset for the year 2000

# .loc after Label
# .iloc ist after row Zeile!
































