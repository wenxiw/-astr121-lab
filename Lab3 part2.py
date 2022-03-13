#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 12:27:43 2022

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



#Unknown 2
N2 = np.loadtxt("/Users/kristy/Downloads/Unknown Spectra/unknown2.txt")
data2 = np.shape(N2)

wl2 = N2[:,0]
I2 = N2 [:,1]


#m0
m0 = np.loadtxt("/Users/kristy/Downloads/Standard Spectra/m0.txt")
data_m0 = np.shape(m0)

wl_m0 = m0[:,0]
I_m0= m0[:,1]


#m5

m5 = np.loadtxt("/Users/kristy/Downloads/Standard Spectra/m5.txt")
data_m5 = np.shape(m5)

wl_m5 = m5[:,0]
I_m5= m5[:,1]


plt.figure()
plt.title("intensity vs. wavelengths")
plt.xlabel("wavelengths (Angstroms)")
plt.ylabel("Normalized Intensity")
plt.plot(wl2, I2 ,label= "unknown2", color = "blue")
plt.plot(wl_m0, I_m0,label= "m0", color = "red")
plt.plot(wl_m5, I_m5 ,label= "m5", color = "green")
plt.legend()

#residual
r_m0 = I_m0 - I2
r_m5 = I_m5 - I2

plt.figure()
plt.title("residual2")
plt.xlabel("wavelengths (Angstroms)")
plt.ylabel("difference")
plt.plot(wl2, r_m0 ,label= "residual m0", color = "red")
plt.plot(wl2, r_m5 ,label= "residual m5", color = "green")
plt.legend()

square_rm0 = sum(r_m0**2)
square_rm5 = sum(r_m5**2)

print(square_rm0)
print(square_rm5)



#Unknown 3
N3 = np.loadtxt("/Users/kristy/Downloads/Unknown Spectra/unknown3.txt")
data3 = np.shape(N3)

wl3 = N3[:,0]
I3 = N3 [:,1]


#g6
g6 = np.loadtxt("/Users/kristy/Downloads/Standard Spectra/g6.txt")
data_g6 = np.shape(g6)

wl_g6 = g6[:,0]
I_g6 = g6[:,1]

#g0

g0 = np.loadtxt("/Users/kristy/Downloads/Standard Spectra/g0.txt")
data_g0 = np.shape(g0)

wl_g0 = g0[:,0]
I_g0= g0[:,1]


plt.figure()
plt.title("intensity vs. wavelengths")
plt.xlabel("wavelengths (Angstroms)")
plt.ylabel("Normalized Intensity")
plt.plot(wl3, I3 ,label= "unknown3", color = "blue")
plt.plot(wl_g6, I_g6 ,label= "g6", color = "red")
plt.plot(wl_g0, I_g0 ,label= "g0", color = "green")
plt.legend()



#residual
r_g6 = I_g6 - I3
r_g0 = I_g0 - I3


plt.figure()
plt.title("residual3")
plt.xlabel("wavelengths (Angstroms)")
plt.ylabel("difference")
plt.plot(wl3, r_g6 ,label= "residual g6", color = "red")
plt.plot(wl3, r_g0 ,label= "residual g0", color = "green")
plt.legend()


square_rg6 = sum(r_g6**2)
square_rg0 = sum(r_g0**2)


print(square_rg6)
print(square_rg0)


#Unknown 4
N4 = np.loadtxt("/Users/kristy/Downloads/Unknown Spectra/unknown4.txt")
data4 = np.shape(N4)

wl4 = N4[:,0]
I4 = N4 [:,1]


#a1
a1 = np.loadtxt("/Users/kristy/Downloads/Standard Spectra/a1.txt")
data_a1 = np.shape(a1)

wl_a1 = a1[:,0]
I_a1 = a1[:,1]


#a5

a5 = np.loadtxt("/Users/kristy/Downloads/Standard Spectra/a5.txt")
data_a5 = np.shape(a5)

wl_a5 = a5[:,0]
I_a5= a5[:,1]


plt.figure()
plt.title("intensity vs. wavelengths")
plt.xlabel("wavelengths (Angstroms)")
plt.ylabel("Normalized Intensity")
plt.plot(wl4, I4 ,label= "unknown4", color = "blue")
plt.plot(wl_a1, I_a1,label= "a1", color = "red")
plt.plot(wl_a5, I_a5 ,label= "a5", color = "green")
plt.legend()

#residual
r_a1 = I_a1 - I4
r_a5 = I_a5 - I4

plt.figure()
plt.title("residual4")
plt.xlabel("wavelengths (Angstroms)")
plt.ylabel("difference")
plt.plot(wl4, r_a1 ,label= "residual a1", color = "red")
plt.plot(wl4, r_a5 ,label= "residual a5", color = "green")
plt.legend()

square_ra1 = sum(r_a1**2)
square_ra5 = sum(r_a5**2)

print(square_ra1)
print(square_ra5)



#Unknown 5
N5 = np.loadtxt("/Users/kristy/Downloads/Unknown Spectra/unknown5.txt")
data5 = np.shape(N5)

wl5 = N5[:,0]
I5 = N5 [:,1]


#k5
k5 = np.loadtxt("/Users/kristy/Downloads/Standard Spectra/k5.txt")
data_k5 = np.shape(k5)

wl_k5 = k5[:,0]
I_k5 = k5[:,1]


#m0

m0 = np.loadtxt("/Users/kristy/Downloads/Standard Spectra/m0.txt")
data_m0 = np.shape(m0)

wl_m0 = m0[:,0]
I_m0 =m0[:,1]



plt.figure()
plt.title("intensity vs. wavelengths")
plt.xlabel("wavelengths (Angstroms)")
plt.ylabel("Normalized Intensity")
plt.plot(wl5, I5 ,label= "unknown5", color = "blue")
plt.plot(wl_k5, I_k5,label= "k5", color = "red")
plt.plot(wl_m0, I_m0 ,label= "m0", color = "green")
plt.legend()

#residual
r_k5 = I_k5 - I5
r_m0 = I_m0 - I5

plt.figure()
plt.title("residual5")
plt.xlabel("wavelengths (Angstroms)")
plt.ylabel("difference")
plt.plot(wl5, r_k5 ,label= "residual k5", color = "red")
plt.plot(wl5, r_m0 ,label= "residual m0", color = "green")
plt.legend()

square_rk5 = sum(r_k5**2)
square_rm0 = sum(r_m0**2)


print(square_rk5)
print(square_rm0)








