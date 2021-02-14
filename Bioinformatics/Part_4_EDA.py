# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 10:31:27 2021

@author: Björn Düsenberg
"""

#%% Bioinformatic Project - Coronavirus
# Using the https://www.ebi.ac.uk/chembl/ Database
# Before the first use:
# pip install chembl_webresource_client
# Project in accordance to the "Bioinformatics Project" from Dataprofessor
# https://www.youtube.com/playlist?list=PLtqF5YXg7GLlQJUv9XJ3RWdd5VYGwBHrP
# Created in Spyder (Python 3.8)

#%% Part 2 - EDA

#%% Import libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style = 'ticks')

#%% Load Data

df_final = pd.read_csv("bioactivity_final_data.csv")

#%% Create dataframe from active and inactive class

df_2class = df_final[df_final.bioactivity_class != 'intermediate']

#%% Frequency plot - Bioactivity Class

plt.figure(figsize = (5.5, 5.5))

sns.countplot(data = df_2class, x = 'bioactivity_class', edgecolor = "black")
plt.xlabel("Bioactivity class", fontsize = 12, fontweight = "bold")
plt.ylabel("Frequency", fontsize = 12, fontweight = "bold")

# plt.savefig("Plot_Bioactivity_Class.pdf")

# Just a few are active

#%% Scatter plot - MW / LogP

plt.figure(figsize = (5.5, 5.5))

sns.scatterplot(data = df_2class,
                x = 'MW',
                y = "LogP",
                hue = "bioactivity_class",
                size = "pIC50",
                alpha = 0.7,
                edgecolor = "black")

plt.xlabel("MW", fontsize = 12, fontweight = "bold")
plt.ylabel("LogP", fontsize = 12, fontweight = "bold")
plt.legend(bbox_to_anchor = (1.05, 1), loc = 2, borderaxespad = 0)

# plt.savefig("Plot_MW_LogP.pdf", bbox_inches="tight")

# There are big and small molecules wich are active against the corona virus

#%% Statistical Analysis with the Mann-Whitney U Test

# Formula / Function according to:
# https://machinelearningmastery.com/nonparametric-statistical-significance-tests-in-python/

def mannwhitney(descriptor, verbose = False):
    from numpy.random import seed
    from scipy.stats import mannwhitneyu
    
# seed the random number generator
    seed(1)
    
# actives and inactives
    selection = [descriptor, "bioactivity_class"]
    df = df_2class[selection]
    active = df[df.bioactivity_class == "active"]
    active = active[descriptor]
    
    selection = [descriptor, "bioactivity_class"]
    df = df_2class[selection]
    inactive = df[df.bioactivity_class == "inactive"]
    inactive = inactive[descriptor]
        
# compare samples
    stat, p = mannwhitneyu(active, inactive)
    print('Statistics=%.3f, p=%.3f' % (stat, p))


# interpret
    alpha = 0.05
    if p > alpha:
        print('Same distribution (fail to reject H0)')
    else:
        print('Different distribution (reject H0)')
        
#%% Boxplots - On Lipinski Parameters - pIC50

plt.figure(figsize = (5.5, 5.5))

sns.boxplot(data = df_2class,
            x = 'bioactivity_class',
            y = "pIC50")

plt.xlabel("Bioactivity class", fontsize = 12, fontweight = "bold")
plt.ylabel("pIC50 Value", fontsize = 12, fontweight = "bold")

# plt.savefig("Plot_Bioactivity_pIC50.pdf")

# Shows the threshold (as expected) between active and inactive molecules
#%% Use the Mann-Whitney U Test on pIC50
mannwhitney("pIC50")

# Reject H0 -> Different distributions

#%% Boxplots - On Lipinski Parameters - LogP

plt.figure(figsize = (5.5, 5.5))

sns.boxplot(data = df_2class,
            x = 'bioactivity_class',
            y = "LogP")

plt.xlabel("Bioactivity class", fontsize = 12, fontweight = "bold")
plt.ylabel("LogP", fontsize = 12, fontweight = "bold")

# plt.savefig("Plot_Bioactivity_LogP.pdf")

# Shows the threshold (as expected) between active and inactive molecules
#%% Use the Mann-Whitney U Test on LogP
mannwhitney("LogP")

# Fail to reject H0 -> Same distributions

#%% Boxplots - On Lipinski Parameters - MW

plt.figure(figsize = (5.5, 5.5))

sns.boxplot(data = df_2class,
            x = 'bioactivity_class',
            y = "MW")

plt.xlabel("Bioactivity class", fontsize = 12, fontweight = "bold")
plt.ylabel("MW", fontsize = 12, fontweight = "bold")

# plt.savefig("Plot_Bioactivity_MW.pdf")

# Shows the threshold (as expected) between active and inactive molecules
#%% Use the Mann-Whitney U Test on MW
mannwhitney("MW")

# Reject H0 -> Different distributions

#%% Boxplots - On Lipinski Parameters - NumHAcceptors

plt.figure(figsize = (5.5, 5.5))

sns.boxplot(data = df_2class,
            x = 'bioactivity_class',
            y = "NumHAcceptors")

plt.xlabel("Bioactivity class", fontsize = 12, fontweight = "bold")
plt.ylabel("NumHAcceptors", fontsize = 12, fontweight = "bold")

# plt.savefig("Plot_Bioactivity_NumHAcceptors.pdf")

# Shows the threshold (as expected) between active and inactive molecules
#%% Use the Mann-Whitney U Test on pIC50
mannwhitney("NumHAcceptors")

# Reject H0 -> Different distributions

#%% Boxplots - On Lipinski Parameters - NumHDonors

plt.figure(figsize = (5.5, 5.5))

sns.boxplot(data = df_2class,
            x = 'bioactivity_class',
            y = "NumHDonors")

plt.xlabel("Bioactivity class", fontsize = 12, fontweight = "bold")
plt.ylabel("NumHDonors", fontsize = 12, fontweight = "bold")

# plt.savefig("Plot_Bioactivity_pIC50.pdf")

# Shows the threshold (as expected) between active and inactive molecules
#%% Use the Mann-Whitney U Test on pIC50
mannwhitney("NumHDonors")

# Reject H0 -> Different distributions






























    
    











































