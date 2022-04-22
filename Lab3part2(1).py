#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 19:00:32 2022

@author: Wenxi Wu
"""
import numpy as np
import matplotlib.pyplot as plt


#Unknown 1
N1 = np.loadtxt("/Users/kristy/Downloads/Unknown Spectra/unknown1.txt")
data1 = np.shape(N1)

wl1 = N1[:,0]
I1 = N1 [:,1]


#b0

b0 = np.loadtxt("/Users/kristy/Downloads/Standard Spectra/b0.txt")
data_b0 = np.shape(b0)

wl_b0 = b0[:,0]
I_b0= b0[:,1]

#o5
o5 = np.loadtxt("/Users/kristy/Downloads/Standard Spectra/o5.txt")
data_o5 = np.shape(o5)

wl_o5 = o5[:,0]
I_o5= o5[:,1]


plt.figure()
plt.title("intensity vs. wavelengths")
plt.xlabel("wavelengths (Angstroms)")
plt.ylabel("Normalized Intensity")
plt.plot(wl1, I1 ,label= "unknown1", color = "blue")
plt.plot(wl_b0, I_b0 ,label= "b0", color = "red")
plt.plot(wl_o5, I_o5 ,label= "o5", color = "green")
plt.legend()


#residual
r_b0 = I_b0 - I1
r_o5 = I_o5 - I1


plt.figure()
plt.title("residual1")
plt.xlabel("wavelengths (Angstroms)")
plt.ylabel("difference")
plt.plot(wl1, r_b0 ,label= "residual b0", color = "red")
plt.plot(wl1, r_o5 ,label= "residual o5", color = "green")
plt.legend()

square_rb0 = sum(r_b0**2)
square_ro5 = sum(r_o5**2)

print(square_rb0)
print(square_ro5)
