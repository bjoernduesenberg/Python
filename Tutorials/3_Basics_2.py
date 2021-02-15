# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 10:43:44 2021

@author: Björn Düsenberg
"""

#%% Tupel

# Variables
firstname = "Max"
lastname = "Mustermann"

firstname2 = "Monika"
lastname2 = "Mustermann"

# Lists
student1 = ["Max", "Mustermann"]
student2 = ["Monika", "Mustermann"]

# --> Changeable

# Tupel are inchangeable! --> round brackets ()

student1 = ("Max", "Mustermann")
student2 = ("Monika", "Mustermann")

#%% Tupel unpack

student1 = ("Max", "Mustermann")

# Assigning a tuple content with indexing --> Labour-intensive
student1_firstname = student1[0]
student1_lastname = student1[1]

print(student1_firstname + " " + student1_lastname)

# Direct allocation
student1_firstname, student1_lastname = student1

#%% Dictionaries 1.1

# Not practicable with loose variables
river = "Fluss"
city = "Stadt"

# --> Assignment in dictionaries
# dictionary = {"key": "value"}

words = {"river": "Fluss",
         "city": "Stadt"}


print(words["river"]) # You have to access the key - no index

# Expand the dictionaries
# dictionary["new key"] = "new value"

words["country"] = "Land"

# Access dictionary dynamically

w = "city"
print(words[w])

# Print the complete dictionary

for key, value in words.items():
    print("key: " + key + ", value: " + value)
   
# List with the content of the dictionary
print(list(words.items()))

#%% Dictionaries 1.2

words = {"river": "Fluss",
         "city": "Stadt"}

# Which keys/values are already used?
print(words.keys())
print(words.values())

# as Liste
print(list(words.keys()))
print(list(words.values()))

# Queries in dictionaries
print("city" in words)
print("country" in words)

#%% Dictionaries 1.3

# if-statements
if not "mobile phone" in words:
    words["mobile phone"] = "Handy"

#%% Dictionaries 1.4

# in dictionaries can also be other data types

words["xyz"] = ["Test", "Hallo Welt"]
words[14] = "..." # Zahlen
words["14"] = "---" # Strings

# Delete value from dictionary
del words[14]









