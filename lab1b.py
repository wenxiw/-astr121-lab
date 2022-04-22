#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 11:06:54 2022

@author: Wenxi Wu
"""
import numpy as np
import matplotlib.pyplot as plt

# A = amplitue
# p = period
# t = time

def function(t,A,p):
    y = A*np.sin(((2*np.pi)*t)/p)
    return y


t = np.linspace(0,30,40)
A = np.random.uniform(12,18,40)
p = 15

y = function(t,A,p)

plt.figure()
plt.plot(t, y,'o', color = "blue",label="randomized data")
plt.title("Relative speed vs. time")
plt.xlabel("Time (days)")
plt.ylabel("Relative Speed((10^1)m/s)")

e = np.std(A)
plt.errorbar(t, y, yerr = e, fmt = '.')


# fitting the curve
from scipy.optimize import curve_fit

def fit_func(t,A,p):
    results = A*np.sin(((2*np.pi)*t)/p)
    return results

popt,pcov = curve_fit(fit_func, t, y, p0=[20,30]) 
y_fit = fit_func(t,*popt)
plt.plot(t,y_fit,label = "curve fit")
plt.legend()

#1 sigma value
sig = np.sqrt(np.diag(pcov))
print(sig)





