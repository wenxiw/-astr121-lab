#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 11:54:51 2022

@author: Wenxi Wu
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import json
with open('/Users/kristy/Downloads/isochrones.json', 'r') as f:
    isoc = json.load(f)

#m45    
m45 = pd.read_table("/Users/kristy/Downloads/m45.txt",sep = '\t')
na_values=''
B_m45 = m45.B
V_m45 = m45.V

B_minus_V = B_m45 - V_m45

two_e8 = isoc['e8']['two']
B_two_e8 = np.array(isoc['e8']['two']['B'])
V_two_e8 = np.array(isoc['e8']['two']['V'])
B_minus_V_two_e8 = B_two_e8 - V_two_e8

plt.figure()
plt.title("V vs. B-V ")
plt.xlabel("B-V")
plt.ylabel("V")
plt.ylim(20,-5)
plt.scatter(B_minus_V,V_m45 - 5.6,label= "V_m45 vs. B-V_m45 ;shifted down by 5.6", color = "blue")
plt.scatter(B_minus_V_two_e8,V_two_e8,label= "V_2e8 vs. B-V_2e8", color = "orange")
plt.legend()


#m67
m67 = pd.read_table("m67.txt",sep = '\t',usecols=['B','V'], na_values =' ')
B_m67 = m67.B
V_m67 = m67.V
B_minus_V_67 = B_m67 - V_m67

threept5_e9 = isoc['e9']['threept5']
B_threept5_e9 = np.array(isoc['e9']['threept5']['B'])
V_threept5_e9 = np.array(isoc['e9']['threept5']['V'])
B_minus_V_threept5_e9 = B_threept5_e9 - V_threept5_e9

plt.figure()
plt.title("V vs. B-V ")
plt.xlabel("B-V")
plt.ylabel("V")
plt.ylim(13,-5)
plt.scatter(B_minus_V_67,V_m67-9.6,label= "V_m67 vs. B-V_m67; shifted down by 9.6", color = "green")
plt.scatter(B_minus_V_threept5_e9,V_threept5_e9,label= "V_3.5e9 vs. B-V_3.5e9", color = "black")
plt.legend()
