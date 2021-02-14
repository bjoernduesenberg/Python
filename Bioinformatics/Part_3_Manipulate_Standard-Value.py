# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 19:46:03 2021

@author: Björn Düsenberg
"""

#%% Bioinformatic Project - Coronavirus
# Using the https://www.ebi.ac.uk/chembl/ Database
# Before the first use:
# pip install chembl_webresource_client
# Project in accordance to the "Bioinformatics Project" from Dataprofessor
# https://www.youtube.com/playlist?list=PLtqF5YXg7GLlQJUv9XJ3RWdd5VYGwBHrP
# Created in Spyder (Python 3.8)

#%% Part 3 - Processing the Dataframe with rdkit to better interprete the data

#%% Import libraries

import pandas as pd
import numpy as np
from rdkit import Chem

from rdkit.Chem import Descriptors, Lipinski

#%% Load Data

df_preprocessed = pd.read_csv("bioactivity_preprocessed_data.csv")

#%% Calculate the Lipinski desciptors

# Lipinski's rule of five, also known as Pfizer's rule of five or simply the rule of five (RO5), 
# is a rule of thumb to evaluate druglikeness or determine if a chemical compound with a 
# certain pharmacological or biological activity has chemical properties and physical 
# properties that would make it a likely orally active drug in humans. 
# The rule was formulated by Christopher A. Lipinski in 1997, based on the observation 
# that most orally administered drugs are relatively small and moderately lipophilic molecules.
# https://en.wikipedia.org/wiki/Lipinski%27s_rule_of_five

def lipinski(smiles, verbose = False):
    
    moldata = []
    for element in smiles:
        mol = Chem.MolFromSmiles(element)
        moldata.append(mol)
        
    baseData = np.arange(1,1)
    i = 0
    
    for mol in moldata:
        desc_MolWt = Descriptors.MolWt(mol)
        desc_MolLogP = Descriptors.MolLogP(mol)
        desc_NumHDonors = Lipinski.NumHDonors(mol)
        desc_NumHAcceptors = Lipinski.NumHAcceptors(mol)
        
        row = np.array([desc_MolWt,
                        desc_MolLogP,
                        desc_NumHDonors,
                        desc_NumHAcceptors])
    
        if(i == 0):
            baseData = row
        else:
            baseData = np.vstack([baseData, row])
        i = i + 1
            
    columnNames = ["MW", "LogP", "NumHDonors", "NumHAcceptors"]
    descriptors = pd.DataFrame(data = baseData, columns = columnNames)
    
    return descriptors

#%% Create Lipinski Data Frame

df_lipinksi = lipinski(smiles = df_preprocessed.canonical_smiles)

# MW - Size of the molecule
# LogP - Solubility
# H Donors and H Acceptors on the molecule

#%% Combine the DataFrames

df_combined = pd.concat([df_preprocessed, df_lipinksi], axis = 1)

#%% Convert IC50 to pIC50 through negative logarithm
# Makes the distrubution more even

def pIC50(input):
    
    pIC50 = []
    
    for i in input['standard_value_norm']:
        molar = i * (10**-9) # Converts nM to M
        pIC50.append(-np.log10(molar))
        
    input['pIC50'] = pIC50
    x = input.drop('standard_value_norm', 1)
    
    return x

#%% Cap the values to prevent getting negatives

# print(df_combined.standard_value.describe())

def norm_value(input):
    
    norm = []
    
    for i in input['standard_value']:
        if i > 100000000:
            i = 100000000
        norm.append(i)
        
    input['standard_value_norm'] = norm
    x = input.drop('standard_value', 1)
    
    return x

#%% Create df_norm
    
df_norm = norm_value(df_combined)

# Max. value will be 100000000
# print(df_combined.standard_value_norm.describe())

#%% Create df_final standard_value column is delited and transformed into pIC50

df_final = pIC50(df_norm)

#%% Safe Dataframe

df_final.to_csv("bioactivity_final_data.csv", index = False)










    
    
    
    
    
    
    
    
    
    
    
    
    