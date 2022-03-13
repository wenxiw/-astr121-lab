#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 11:02:49 2022

@author: Wenxi Wu
"""
import numpy as np
import matplotlib.pyplot as plt

#A0 star
def intensity(wavelengths, t_A0):
    I_A0 = ((2*h*c**2)/(wavelengths**5))*(1/((np.exp((h*c)/(wavelengths*k*t_A0)))-1))
    return I_A0


wavelengths = np.linspace((1*10**(-10)),(1.5*10**(-6)),100)
t_A0 = 10000
h = 6.626*10**(-34)
c = 3*10**8
k = 1.381*10**(-23)

I_A0 = intensity(wavelengths, t_A0)


#Sun
def intensity(wavelengths, t_Sun):
    I_Sun = ((2*h*c**2)/(wavelengths**5))*(1/((np.exp((h*c)/(wavelengths*k*t_Sun)))-1))
    return I_Sun


wavelengths = np.linspace((1*10**(-10)),(1.5*10**(-6)),100)
t_Sun = 5780
h = 6.626*10**(-34)
c = 3*10**8
k = 1.381*10**(-23)

I_Sun = intensity(wavelengths, t_Sun)


#M0 star
def intensity(wavelengths, t_M0):
    I_M0 = ((2*h*c**2)/(wavelengths**5))*(1/((np.exp((h*c)/(wavelengths*k*t_M0)))-1))
    return I_M0


wavelengths = np.linspace((1*10**(-10)),(1.5*10**(-6)),100)
t_M0 = 3750
h = 6.626*10**(-34)
c = 3*10**8
k = 1.381*10**(-23)

I_M0 = intensity(wavelengths, t_M0)

plt.title("intensity vs. wavelengths")
plt.xlabel("wavelengths (m)")
plt.ylabel("intensity (w m^-3 sr^-1))")

plt.plot(wavelengths, I_A0 , '--', label= "A0", color = "blue")
plt.plot(wavelengths, I_Sun, ':', label= "Sun", color = "orange")
plt.plot(wavelengths, I_M0, label = "M0", color = "red")
plt.legend()
plt.show()


# Theory B0 star

def I(wavelength, t_B0):
    i_B0 = ((2*h*c**2)/(wavelength**5))*(1/((np.exp((h*c)/(wavelength*k*t_B0)))-1))
    return i_B0


wavelength = np.linspace(3900,4500,600)
t_B0 = 29000
h = 6.626*10**(-34)
c = 3*10**8
k = 1.381*10**(-23)
i_B0 = I(wavelength, t_B0)
normal_i = i_B0/(1.038687*10**(-24))

#B0 star
n = np.loadtxt("/Users/kristy/Downloads/Standard Spectra/b0.txt")
data = np.shape(n)

wl = n[:,0]
I = n[:,1]


plt.figure()
plt.title("intensity vs. wavelengths (B0)")
plt.xlabel("wavelengths (Angstroms)")
plt.ylabel("Normalized Intensity")
plt.plot(wl, I ,label= "b0", color = "blue")
plt.plot(wavelength, normal_i ,label= "b0_theory", color = "red")
plt.legend()


