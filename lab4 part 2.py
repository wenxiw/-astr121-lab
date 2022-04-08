#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 12:54:12 2022

@author: Wenxi Wu
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import json
with open('/Users/kristy/Downloads/isochrones.json', 'r') as f:
    isoc = json.load(f)
    
#step1
five = isoc['e9']['five']
B_e9 = np.array(isoc['e9']['five']['B'])
V_e9 = np.array(isoc['e9']['five']['V'])
B_minus_V_e9 = B_e9 - V_e9

ninept5 = isoc['e9']['ninept5']
B_ninept5 = np.array(isoc['e9']['ninept5']['B'])
V_ninept5 = np.array(isoc['e9']['ninept5']['V'])
B_minus_V_ninept5 = B_ninept5 - V_ninept5

two_e8 = isoc['e8']['two']
B_two_e8 = np.array(isoc['e8']['two']['B'])
V_two_e8 = np.array(isoc['e8']['two']['V'])
B_minus_V_two_e8 = B_two_e8 - V_two_e8

seven_e8 = isoc['e8']['seven']
B_seven_e8 = np.array(isoc['e8']['seven']['B'])
V_seven_e8 = np.array(isoc['e8']['seven']['V'])
B_minus_V_seven_e8 = B_seven_e8 - V_seven_e8

m45 = pd.read_table("/Users/kristy/Downloads/m45.txt",sep = '\t')
na_values=''
B_m45 = m45.B
V_m45 = m45.V

B_minus_V = B_m45 - V_m45

plt.figure()
plt.title("V vs. B-V ")
plt.xlabel("B-V")
plt.ylabel("V")
plt.ylim(15,-5)
plt.scatter(B_minus_V_e9,V_e9,label= "V_e9 vs. B-V_e9", color = "blue")
plt.scatter(B_minus_V_ninept5,V_ninept5,label= "V_ninept5 vs. B-V_ninept5", color = "red")
plt.scatter(B_minus_V_two_e8,V_two_e8,label= "V_two_e8 vs. B-V_two_e8", color = "orange")
plt.scatter(B_minus_V_seven_e8,V_seven_e8,label= "V_seven_e8 vs. B-V_seven_e8", color = "green")
plt.scatter(B_minus_V,V_m45,label= "V vs. B-V", color = "blue")
plt.legend()

#step3
m = 5 *np.log10(4)+V_e9
B_minus_m = B_e9 - m

plt.figure()
plt.title("V vs. B-m ")
plt.xlabel("B-m")
plt.ylabel("V")
plt.ylim(20,-5)
plt.scatter(B_minus_m ,m,label= "m vs. B-m", color = "blue")
