#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 11:03:39 2022

@author: Wenxi Wu
"""

import numpy as np

'''
text = "Hello World!"
integer = 1
my_float = 2.35

print(text)
print(integer)
print(my_float)


x = 5
y = 6

print(x + y)


x = 5
y = 6
z = x + y

print(z)


x = 5
y = 6

print(x + y) 
print(x - y) 
print(x * y) 
print(x / y) 
print(x ** y) 
print(x % y) 

x = 5
y = "Banana"

print(x + y)

text = "Hello World!"

print(text)
print(len(text))
print(text.upper())
print(text.lower())

fruit = "Apples"
vegetable = "Potatoes"

shoppinglist = fruit + "\n" + vegetable

print(shoppinglist)


text = "Hello World!"

print(text)
print(text[0])
print(text[1])
print(text[2:4])
print(text[:6]) 
print(text[7:]) 
print(text[-1]) 


shopping=["Apples","Potatoes","Bananas","Biscuits"]

print(shopping[0])
print(shopping[3]) 
print(shopping[1:3]) 
print(shopping[-1]) 


shopping=["Apples","Potatoes","Bananas","Biscuits"]

print(shopping)
print(len(shopping))

shopping.append("Strawberries")
print(shopping)
print(len(shopping))

shopping.extend(["Gravy","Lemonade"])
print(shopping)
print(len(shopping))

shopping.sort()
print(shopping)
print(len(shopping))

shopping.reverse()
print(shopping)
print(len(shopping))

c = [0,1,2,3,4,5,6,7,8,9]
d = c**2
print(d)

'''
'''
import numpy as np
'''
'''
c = [0,1,2,3,4,5,6,7,8,9]
c = np.array(c)
d = c**2

print(d)


x = np.arange(0,10,1)
y = np.linspace(0,10,11)

print(x)
print(y)

'''
x = np.array([[10,20,30],[40,50,60]])
print(x)

'''
a = np.zeros(10)
print(a)


b = np.ones((2,3))
print(b)

c = np.full((2,2),7)
print(c)

d = np.random.random(5)
print(d)

e = np.random.uniform(-2,2,10)
print(e)

a[0]=7
print(a)


path = "./timeseries_data.txt"
astrodata = np.loadtxt(path)

print(astrodata.shape)

t = astrodata[0,:]
signal = astrodata[1,:]

np.savetxt("my_timeseries_data.txt", astrodata)


print(np.sqrt(25))

print(np.sin(np.pi/2))


a = np.array([3,7,1,5,2,9,6])
print(np.sum(a))

a_sort = np.sort(a)
print(a_sort)


def length(x,y):
    return np.sqrt(x**2 + y**2)

g = length(3,4)
print(g)


def my_fn(a,b):
    sum = a + b
    product = a * b
    return sum, product

S, P = my_fn(3,4)
print(S)
print(P)
'''








