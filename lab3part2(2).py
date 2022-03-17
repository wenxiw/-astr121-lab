#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 20:36:43 2022

@author: Wenxi Wu
"""

import numpy as np


#a1
a1 = np.loadtxt("/Users/kristy/Downloads/Standard Spectra/a1.txt")
data_a1 = np.shape(a1)

I_a1 = a1[:,1]


#a5

a5 = np.loadtxt("/Users/kristy/Downloads/Standard Spectra/a5.txt")
data_a5 = np.shape(a5)

wl_a5 = a5[:,0]
I_a5= a5[:,1]

#b0
b0 = np.loadtxt("/Users/kristy/Downloads/Standard Spectra/b0.txt")
data_b0 = np.shape(b0)

wl_b0 = b0[:,0]
I_b0= b0[:,1]

#b6
b6 = np.loadtxt("/Users/kristy/Downloads/Standard Spectra/b6.txt")
data_b6 = np.shape(b6)

wl_b6 = b6[:,0]
I_b6 = b6[:,1]

#o5
o5 = np.loadtxt("/Users/kristy/Downloads/Standard Spectra/o5.txt")
data_o5 = np.shape(o5)

wl_o5 = o5[:,0]
I_o5= o5[:,1]

#f0
f0 = np.loadtxt("/Users/kristy/Downloads/Standard Spectra/f0.txt")
data_f0 = np.shape(f0)

wl_f0 = f0[:,0]
I_f0= f0[:,1]

#f5
f5 = np.loadtxt("/Users/kristy/Downloads/Standard Spectra/f5.txt")
data_f5 = np.shape(f5)

wl_f5 = f5[:,0]
I_f5= f5[:,1]

#g0

g0 = np.loadtxt("/Users/kristy/Downloads/Standard Spectra/g0.txt")
data_g0 = np.shape(g0)

wl_g0 = g0[:,0]
I_g0= g0[:,1]

#g6
g6 = np.loadtxt("/Users/kristy/Downloads/Standard Spectra/g6.txt")
data_g6 = np.shape(g6)

wl_g6 = g6[:,0]
I_g6 = g6[:,1]

#k0

k0 = np.loadtxt("/Users/kristy/Downloads/Standard Spectra/k0.txt")
data_k0 = np.shape(k0)

wl_k0 = k0[:,0]
I_k0= k0[:,1]

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

#m5

m5 = np.loadtxt("/Users/kristy/Downloads/Standard Spectra/m5.txt")
data_m5 = np.shape(m5)

wl_m5 = m5[:,0]
I_m5= m5[:,1]

#o5
o5 = np.loadtxt("/Users/kristy/Downloads/Standard Spectra/o5.txt")
data_o5 = np.shape(o5)

wl_o5 = o5[:,0]
I_o5= o5[:,1]



#Unknown 1
N1 = np.loadtxt("/Users/kristy/Downloads/Unknown Spectra/unknown1.txt")
data1 = np.shape(N1)

wl1 = N1[:,0]
I1 = N1 [:,1]

#Unknown 2
N2 = np.loadtxt("/Users/kristy/Downloads/Unknown Spectra/unknown2.txt")
data2 = np.shape(N2)

wl2 = N2[:,0]
I2 = N2 [:,1]

#Unknown 3
N3 = np.loadtxt("/Users/kristy/Downloads/Unknown Spectra/unknown3.txt")
data3 = np.shape(N3)

wl3 = N3[:,0]
I3 = N3 [:,1]

#Unknown 4
N4 = np.loadtxt("/Users/kristy/Downloads/Unknown Spectra/unknown4.txt")
data4 = np.shape(N4)

wl4 = N4[:,0]
I4 = N4 [:,1]

#Unknown 5
N5 = np.loadtxt("/Users/kristy/Downloads/Unknown Spectra/unknown5.txt")
data5 = np.shape(N5)

wl5 = N5[:,0]
I5 = N5 [:,1]

data = [I_a1, I_a5, I_b0, I_b6, I_f0, I_f5, I_g0, I_g6, I_k0, I_k5, I_m0, I_m5, I_o5]

I = [I1, I2, I3, I4, I5]

I_full_list = []
for each_I in I:
    data_sum_squared = []
    for lst in data:
        r = lst - each_I
        s = 0
        for x in r:
            s = s + (x**2)
        data_sum_squared.append(s)
    I_full_list.append(data_sum_squared)

index = 1
for l in I_full_list:
    print(f"{index}: {l}\n")
    index = index + 1


    

          
          
          
