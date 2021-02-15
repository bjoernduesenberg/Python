# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 20:35:12 2021

@author: Björn Düsenberg 
"""
#%% Basic calculations
print(5+4)
print(5-4)
print(5*4)
print(5/4)

#%% Exponentiate
print(5 ** 4)

# Modulo --> Remainder for integer division
print(5 % 4)

#%% Round
print(round(4.4))


#%% Import Math module
import math

print(math.ceil(4.4)) # Round up
print(math.floor(4.4)) # Round down

#%% Square root and logarithm

print(math.sqrt(9))
print(math.log(10))

#%% Strings - Crashkurs - 1
print("Hallo Welt")

print("Hallo" + " " + "Welt") # Zusammengesetzter String

# Conversion int to str
print("Hallo" + " " + str(3))

# Print a function - len
print(len("Hallo"))


#%% Strings - Crashkurs - 1.2

# Delete unnecessary spaces
what = "    banana  " # Variable
print(what.strip())

# Everything to upper/lower letters
print(what.upper())
print(what.lower())

# Write back
what = what.strip()
print(what)

# replace("What should be replaced?", "replace with")
print("Hallo Welt Welt".replace("Welt", "Mars"))

# Find function - position
print("Hallo Welt".find("Welt"))

# Count function 
print("Hallo Welt".count("l"))

#%% Strings - Crashkurs - 1.3

# Line break \n
print("Hallo\nWelt")

# Tab \t
print("Hallo\tWelt")

#%% Strings - Crashkurs - 2.1

txt = "Hallo Welt"
print(txt[0]) # Print character at position 0
print(txt[-1]) # Print last character

# Accessing multiple characters
print(txt[0:5])
print(txt[6:10])
print(txt[-5:-1])

#%% Booleans 1.1

b = True
c = False

a = 42
print(a == 42) # Check if is equal to ==
print(a != 42) # Check whether unequal with !=

d = "Hallo"
print(d == "Hallo") # Check if is equal to ==
print(d != "Hallo") # Check whether unequal with !=

#%% Booleans 1.2

# logical and
print(True and True)
print(False and True)
print(True and False)
print(False and False)

# logical or
print(True or True)
print(False or True)
print(True or False)
print(False or False)

# negate with not
print(not True)
print(not False)

#%% if - Statements 1.1

print("Vorher")

if True: # if statement after which expression becomes Boolean
    print("In der if-Abfrage") # If True then the following is executed
    
print("Nachher")

#%% if - Statements 1.2

z = 42

if z <= 50:
    print("Die Variable ist kleiner als 50")

if z <= 50 and z < 70:
    print("Die Variable ist zwischen 40 und 70")
    
txt_2 = "Mit Text"
txt_3 = "" # empty text

if txt_2:
    print("String in txt_2 vorhanden")

if txt_3:
    print("String in txt_2 vorhanden") # nothing is printed
    
p = 42

if p:
    print("...")

#%% if - Statement 1.3

# if else

z = 40

if z >= 50:
    print("z <= 50")
else:
    print("z nicht > 50")

# nest further

if z >= 50:
    print("z <= 50")
else:
    if z < 45:
        print("z > 45")
    else:
        print("z nicht > 45")
        
# if and else pull together

if z > 50:
    print("z > 50")
elif z > 45:
    print("z > 45")
else:
    print("z ist nicht größer 45")

#%% Convert

# Convert to str
a = str(3)

# Convert to int
g = int("3")

# Convert to float
h = float("4.4")
















