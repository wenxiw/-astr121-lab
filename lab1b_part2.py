#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 12:38:39 2022

@author: Wenxi Wu
"""

import numpy as np
import matplotlib.pyplot as plt

#2
#read file lab1_sample.txt
r = np.loadtxt("/Users/kristy/Downloads/lab1_sample.txt")
data = np.shape(r)
print(data) #file consists of 100 rows and 3 colomns

#fre- relative frequency
fre = r[:,0]
#lstr- line strength
lstr = r[:,1]
#sigma- uncertainty
sigma = r[:,2]

#plotting data
plt.figure(2)
plt.legend()
def plot_data():
    plt.plot(fre, lstr, label = "data")
    plt.title("Line strength vs. Frequency")
    plt.xlabel("Relative Frequency")
    plt.ylabel("Line Strength")
    plt.errorbar(fre, lstr, yerr = sigma, fmt =  ".")
plot_data()

#3 plotting Gaussian curve
def function(fre):
    g = 1/(std * np.sqrt(2 * np.pi)) * np.exp( - (fre - mean)**2 / (2 * std**2))
    return g

amp = 0.032
mean = np.mean(fre)
std = np.std(fre)
g = function(fre)

plt.figure(3)
plt.plot(g)


#4 fitting the data
def fit_func(fre, mean, std):
    return 1/(std * np.sqrt(2 * np.pi)) * np.exp( - (fre - mean)**2 / (2 * std**2))

from scipy.optimize import curve_fit

popt,pcov = curve_fit(fit_func, fre, mean, p0=[59, 40]) 

g_fit = fit_func(fre,*popt)


plt.figure(4)
plt.plot(fre, g_fit,label= "curve fit")


#adding fit cuvre to original data
plt.figure(5)
plt.figure(5).clear()
plot_data()
plt.plot(fre, g_fit, label="curve fit")
plt.show()
plt.legend()

#1 sigma value
sig = np.sqrt(np.diag(pcov))
print(sig)
