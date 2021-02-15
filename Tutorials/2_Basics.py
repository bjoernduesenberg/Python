# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 21:27:05 2021

@author: Björn Düsenberg
"""

#%% Lists 1.1

# Variables 
name1 = "Max"
name2 = "Monika"

# Create list
names = []
print(names)

# Fill list
names = ["Max", "Monika", 42] 
print(names)

# Append
names.append("Lisa") # Change the existing list
print(names)

#%% Lists 1.2

# Insert at specific point
names.insert(0, "Claudia")
print(names)

# Delete last element
print(names.pop())
print(names)

#%% Lists 1.3

# Get element
print(names[2])
print(names[2:4])
print(names[1:])

# Length of the list
print(len(names))

# Index from element
print(names.index("Monika"))

# Delete specific element
names.pop(4) 
print(names)

# Searches and removes the element of the brackets, once
names.remove("Max") 
print(names)

#%% Convert

# String to list
l = "Orange, Apfel, Kirsche"
print(l.split(", ")) # string.split("...")

# List to string
l2 = ['Orange', 'Apfel', 'Kirsche']
print(", ".join(l2)) # "Trennzeichen.join(Liste)

# range to list
print(list(range(1, 10)))

#%% for - Statement 1.1

for i in range(1, 11): 
    print("Hallo Welt")

print(list(range(1, 11))) 

for i in [1, 13, 42, 55]: # 4 elements, does not matter what kind of elements
    print("Hallo Welt") # print "Hallo Welt" 4 times

numbers = [1, 13, 42, 55]
for i in numbers: 
    print("Hallo Welt") 

#%% for - Statement 1.2

# Sum with for - statement
summe = 0
for i in range(1, 101):
    summe = summe + i
    print(summe)
    
# sum - function
print(sum(range(1, 101)))

#%% for - Statement 1.3

text = "Hallo Welt"

for i in text: # Output of each individual character in text
    print(i)


for i in text.lower(): # Output of each individual character in text in lower letters
    print(i)

for i in text.upper(): # Output of each individual character in text in upper letters
    print(i)

for i in text: # insert a . after each 
    print(i + ".")

final = ""
for i in text: 
    final = final + i + "."

#%% for - Statement 1.4 

names = ['Max', 'Monika', 'Claudia']

greetings = []

for name in names:
    greetings.append("Hallo " + name)

print(greetings)

# Counts letters in word
length = []

for name in names:
    length.append(len(name))

print(length)

#%% for - Statement 1.5 List comprehensions - higher performance

names = ['Max', 'Monika', 'Claudia']

greetings = ["Hallo " + name for name in names] # integrated for - statement

print(greetings)


length = [len(name) for name in names]
print(length)

#%% for - Statement 1.6

# Greeting f. all names with "M"

names = ['Max', 'Monika', 'Claudia']

greetings = []

for name in names:
    if name[0] == "M":
        greetings.append("Hallo " + name)
        
# OR

greetings = ["Hallo " + name for name in names if name[0] == "M"]

#%% for - Statement 1.7

# Aufgabe -  Alle Zahlen zwischen 1 u. 100 die durch 3 teilbar sind
zahlen = [zahl for zahl in range(1, 101) if zahl % 3 == 0]
print(zahlen)

#%% while - Statement

# Loop is fulfilled until condition is no longer fulfilled

# while True:
    # print("Hello World")
    
# --> Attention - END LOOP

a = 23

while a >= 0:
    print(a)
    a = a - 5

print("...")

#%% break and continue

for i in range(1, 11):
    if i != 5 and i != 8: # Nested query - unclear code
        print("Hallo Welt: " + str(i))
        
for i in range(1, 11):
    if i == 5:
        continue # continue steps
    if i == 8:
        continue 
    print("Hallo Welt: " + str(i))


for i in range(1, 11):
    if i == 5:
        break # break ends loop
    print("Hallo Welt: " + str(i))





