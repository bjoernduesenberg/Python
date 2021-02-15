# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 11:16:58 2021

@author: Björn Düsenberg
"""

#%% Functions 1.1

# Dublicate code
print("Ich bin ein Text")
print("Ich bin ein Text")

# Define the function
def f():
    print("Ich bin ein Text")
    print("Ich bin ein Text")

# Use function
f()

#%% Functions 1.2

# Parameters

def y(x):
    for i in range(0, x):
        print("Ich bin ein Text")
        
# y(3) return 3 times

# Several parameters

def add(a, b):
    print(a + b)

# add(2, 3)

#%% Functions 1.3

# Set default value - used when no entry is made
def y(x = 3):
    for i in range(0, x):
        print("Ich bin ein Text")

# y() - 3-times 
# y(5) - 5-times 

def z(a, b):
    print("a = " + str(a))
    print("b = " + str(b))
 
# Input can be changed by naming in the brackets
z(a = 3, b = 7)

#%% Functions 1.4

# Return - Addition direct after the print statement
def add(parameter_a, parameter_b):
    print(parameter_a + parameter_b)

# Return value
# For example
# import math
# math.sqrt(25) # is calculated but not returned

#%% Functions 1.5

def add(parameter_a, parameter_b):
    return parameter_a + parameter_b

print(add(5, 6) + 5) # the return value in the function is further usable


#%% Read txt - data

# open function
f = open("faust.txt", encoding= "utf-8")
print(type(f))

#%% Read from text

f = open("faust.txt", encoding= "utf-8")

# Output of all lines, line-by-line, in the file
for l in f:
    print(l.strip())
    break # Breaks off after first line - stream needs file every time again
    
#%% Read file

f = open("faust.txt", encoding= "utf-8")

contents = f.read()
print(contents)

f.close()

#%% with-Befehl - automatic close

with open("faust.txt", encoding= "utf-8") as file:
    contents = file.read()
print(contents)

#%% Write in file

with open("datei.txt", mode = "a") as file:
    file.write("Hallo Welt! \n")
    




















































































