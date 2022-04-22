# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 11:03:40 2022

@author: Wenxi Wu
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#step1
m45 = pd.read_table("/Users/kristy/Downloads/m45.txt",sep = '\t')
na_values=''
B_m45 = m45.B
V_m45 = m45.V

B_minus_V = B_m45 - V_m45

plt.figure()
plt.title("V vs. B-V ")
plt.xlabel("B-V")
plt.ylabel("V")
plt.ylim(20,0)
plt.scatter(B_minus_V,V_m45,label= "V vs. B-V", color = "blue")
plt.legend()

#step2
T = 4600*((1/(0.92*0.5+1.7))+(1/(0.92*0.5+0.62)))
print(T)

h = 6.626*10**(-34)
c = 3*10**8
k = 1.381*10**(-23)
wavelengths_full=np.linspace((1*10**(-10)),(1.5*10**(-6)),100)


def intensity(wavelengths, T):
    I = ((2*h*c**2)/(wavelengths**5))*(1/((np.exp((h*c)/(wavelengths*k*T)))-1))
    return I
I = intensity(wavelengths_full, T)

plt.figure()
plt.title("Intensity vs. wavelengths")
plt.xlabel("wavelengths (m) ")
plt.ylabel("Intensities (w m^-3 sr^-1)")
plt.plot(wavelengths_full,I,label= "Intensity vs. wavelengths", color = "red")
plt.legend()



#step3&4
I_normalized = I / (4.356*10**13)

T_new = 4600*((1/(0.92*1+1.7))+(1/(0.92*1+0.62)))
print(T_new)

def intensity(wavelengths, T_new):
    I_n = ((2*h*c**2)/(wavelengths**5))*(1/((np.exp((h*c)/(wavelengths*k*T_new)))-1))
    return I_n
I_new = intensity(wavelengths_full, T_new)

I_new_normalized = I_new/ (9.819*10**(12))


plt.figure()
plt.title("Normalized Intensity vs. wavelengths_BV")
plt.xlabel("wavelengths_BV (m) ")
plt.ylabel("Normalized Intensities (w m^-3 sr^-1)")
plt.plot(wavelengths_full,I_normalized,label= "Normalized Intensity vs. wavelengths_BV", color = "red")
plt.plot(wavelengths_full,I_new_normalized,label= "New Intensity", color = "orange")
plt.axvline(x=4*10**(-7),color = "blue", linestyle= "dashed")
plt.axvline(x=5*10**(-7),color = "blue", linestyle= "dashed")
plt.axvline(x=4.45*10**(-7),color = "blue", linestyle= "solid",label = "B filter")
plt.axvline(x=5*10**(-7),color = "green", linestyle= "dashed")
plt.axvline(x=7*10**(-7),color = "green", linestyle= "dashed")
plt.axvline(x=5.51*10**(-7),color = "green", linestyle= "solid",label = "V filter")
plt.legend()












