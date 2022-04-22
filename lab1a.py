#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 11:06:15 2022

@author: Wenxi Wu
"""
import numpy as np

#3 making 2-dimensional numpy array
A = np.array([[1, 2, 3, 2, 4, 6, 3, 6, 9],[4, 5, 6, 8, 10, 12, 12, 15, 18]])
print(A)


#4 finding Q
B = np.arange(0,10,2)
A = np.array([np.zeros(5),B])
S = A.shape
Q = S[0] + len(B) - A[1,3] + (np.zeros((2,3))).size
print(Q)


#5 randomizing values, sorting an array, and finding mean
d = np.random.random(8) 
d_sort = np.sort(d)
mean = np.mean(d_sort)
print(d)
print(d_sort)
print(mean)


#6 defining a function
def function(x,y):
    y = np.sqrt(x**2 + 15)
    return y


#7
#a making a 2 dimensional array
g = np.array([[1, 4, 7],[3, 5, 8]])
print(g)


#b array from 10 to 50 with an increment of 0.1
b = np.arange(10,50,0.1)
print(b)


#c array from 10 to 50 with 1900 equally spaced points
c = np.linspace(10,50,1900)
print(c)


#d equation 5cosx
d = 5*np.cos(b)
print(d)


#e equation 3y
e = 3*c
print(e)


#f plotting 7d and 7e
import matplotlib.pyplot as plt

plt.figure()
plt.plot(b,d,label = "5cos(c)", color="blue", linestyle="-") 

plt.plot(c,e, color="black", label = "3c", linestyle="dotted") 

plt.title("part f") 
plt.xlabel("x-axis") 
plt.ylabel("y-axis") 
plt.legend() 


#g solution to #6
def function(x):
    y = np.sqrt(x**2 + 15)
    return y
y = function(b)
print(y)


#h plotting 7g and reverse x axis
plt.figure()
plt.plot(b,y,label = "function y", color="blue", linestyle = "-") 
plt.xlim(50,10)

plt.title("part h") 
plt.xlabel("x-axis") 
plt.ylabel("y-axis") 
plt.legend()

