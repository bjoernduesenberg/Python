# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 18:01:59 2021

@author: Björn Düsenberg
"""

#%% Bioinformatic Project - Coronavirus
# Using the https://www.ebi.ac.uk/chembl/ Database
# Before the first use:
# pip install chembl_webresource_client
# Project in accordance to the "Bioinformatics Project" from Dataprofessor
# https://www.youtube.com/playlist?list=PLtqF5YXg7GLlQJUv9XJ3RWdd5VYGwBHrP
# Created in Spyder (Python 3.8)

#%% Part 1 - Create DataSet

#%% Import libraries

import pandas as pd
from chembl_webresource_client.new_client import new_client

#%% Search for the target protein

target = new_client.target
target_query = target.search('coronavirus')
targets = pd.DataFrame.from_dict(target_query)

# Show the column names as a list
print(targets.columns)

# Show the content of the column "target_type" 
print(targets["target_type"])

# We use the Single Protein for the further investigation 

#%% Select the target - ID

select_target = targets.target_chembl_id[4]
print(select_target)

#%% Retrieve the bioactivity data

# Use the IC50 value
# The half maximal inhibitory concentration (IC50) is a measure of the potency 
# of a substance in inhibiting a specific biological or biochemical function
# https://en.wikipedia.org/wiki/IC50

activity = new_client.activity

# Filter for the chembl ID and the IC50 value
res = activity.filter(target_chembl_id = select_target).filter(
    standard_type = "IC50")

# Create dataframe out of this query
df_bioact = pd.DataFrame.from_dict(res)

# Show the column names
print(df_bioact.columns)

# Check if there is just one standard type - IC50
print("The standard type(s) is/are: " + df_bioact.standard_type.unique())

#%% Safe as .csv

df_bioact.to_csv("bioactivity_data.csv", index = False)































