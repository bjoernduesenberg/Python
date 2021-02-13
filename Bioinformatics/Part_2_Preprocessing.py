# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 19:20:05 2021

@author: Björn Düsenberg
"""

#%% Bioinformatic Project - Coronavirus
# Using the https://www.ebi.ac.uk/chembl/ Database
# Before the first use:
# pip install chembl_webresource_client
# Project in accordance to the "Bioinformatics Project" from Dataprofessor
# https://www.youtube.com/playlist?list=PLtqF5YXg7GLlQJUv9XJ3RWdd5VYGwBHrP
# Created in Spyder (Python 3.8)

#%% Part 2 - Preprocessing the Dataframe

#%% Import libraries

import pandas as pd

#%% Load Data

df_bioact = pd.read_csv("bioactivity_data.csv")

#%% Standard value and bioactivity

# Standard value describes the potency in nano molar [nM]
# High standard value = high dosis needed
# Low standard value = low dosis needed --> Thats what we want!
# 0 - 1000 nM = active
# 1000 - 10000 nM = intermediate
# 10000 < x nM = inactive

bioactivity_class = []
for i in df_bioact.standard_value:
    if float(i) >= 10000:
        bioactivity_class.append("inactive")
    elif float(i) <= 1000:
        bioactivity_class.append("active")
    else:
        bioactivity_class.append("intermediate")
        
#%% molecule_chembl_id, canonical_smiles, standard_value

# Each molecule has a molecule_chembl_id 
# We want each ID just once

mol_cid = []
for i in df_bioact.molecule_chembl_id:
    mol_cid.append(i)


# SMILES = Simplified molecular-input line-entry system
# https://en.wikipedia.org/wiki/Simplified_molecular-input_line-entry_system

canonical_smiles = []
for i in df_bioact.canonical_smiles:
    canonical_smiles.append(i)

# See above

standard_value = []
for i in df_bioact.standard_value:
    standard_value.append(i)

#%% Combine lists
selection = list(zip(mol_cid, canonical_smiles, standard_value, bioactivity_class))
df_preprocessed = pd.DataFrame(selection, columns=["molecule_chembl_id",
                                                   "canonical_smiles",
                                                   "standard_value",
                                                   "bioactivity_class"])

#%% Safe as .csv

df_preprocessed.to_csv("bioactivity_preprocessed_data.csv", index = False)














