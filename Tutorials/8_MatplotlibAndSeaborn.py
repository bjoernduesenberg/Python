# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 11:32:12 2021

@author: Björn Düsenberg
"""

#%% Import modules

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns # Seaborn is an extension of matplotlib

# Therefore, matplotlib arguments can also be entered in Seaborn plots

# %matplotlib qt or %matplotlib inline 

#%% Import data

path = "path..."
df = pd.read_csv(path + "diamonds.csv.bz2")

#%% Sample

# df.sample(Samplenumber, random_state = x)
df = df.sample(1000, random_state = 42)

#%% Scatterplot

sns.set()

x = df["carat"]
y = df["price"]

# sns.scatterplot(x, y, alpha = 0.7, marker = "v") # marker is from Matplotlib

# sns.scatterplot(x, y,
                #alpha = 0.7, # transparency
                #style = df["cut"], # Style after input variable
                #markers = True) # markers (plural) is from Seaborn - lists as input  are possible

ax = sns.scatterplot(
        data = df,
        x = "carat", 
        y = "price",
        alpha = 0.7, # Transparency
        s = 100, # Size of all points (from Matplotlib)
        hue = "cut", # Color after parameter
        style = "cut", # Style after input variable
        markers = True) # markers (plural) is from Seaborn - lists as input are possible

ax.set_xlabel("Karat")
ax.set_ylabel("Preis / €")

#%% Bar diagrams

# Summarise the colour of each cut and tell me how many occur.
df_color = df.groupby("color").agg(count = ("cut", len)) 

bx = sns.barplot(x = df_color.index.values,
                 y = df_color["count"])



































