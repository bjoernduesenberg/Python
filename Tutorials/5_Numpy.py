# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 16:01:18 2021

@author: Björn Düsenberg
"""

#%% Intro - import module

import numpy as np

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = x ** 2

print(y)

#%% calculations with Numpy

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

y = np.zeros(10) # 10 times 0
z = np.ones(10) # 10 times 1
u = np.arange(1, 10, 0.5) # Array from 1 to 10 with stepwidth 0.5

xs = np.array([1, 5, 9])
print(xs + np.arange(1, 4, 1))

a = np.arange(1, 4, 1)
print(a)
print(xs <= a)

#%% Exkurs: Plot Data 1.1

%matplotlib inline 

import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [2, 3, 4])
plt.show()

#%% Exkurs: Plot Data 1.2

xs = np.arange(-3, 3, 0.1)
ys = xs ** 3 - xs ** 2 + 6

plt.plot(xs, ys)
plt.show()

#%% Multidimensional data

# import numpy as np

# Matrix
xs = np.array([ 
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [4, 5, 6, 7, 8]])

print(xs.shape)
print(xs[2]) # one row

#%% Reshape

xs = np.array([
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [4, 5, 6, 7, 8]])

print(xs.reshape(-1)) # -1 to convert a line (vector) to a (list)

# Alternatively, enter the number that equals the sum of all fields
print(xs.reshape(15))

# Multidimensional reshape
print(xs.reshape(5, 3))

# Mehrdimensional array to one column
print(xs.reshape(-1, 1))

#%% Numpy operations

print(xs.min())
print(xs.max())
print(xs.mean())

x = np.array([1, 2, 5, 4, 5 ,6 , 7, 0])
print(x.argmax()) # Where is the maximum
print(x.argmin()) # Where is the minimum









