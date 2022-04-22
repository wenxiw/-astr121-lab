#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 19:17:55 2022

@author: Justin Williams
"""

import numpy as np
import matplotlib.pyplot as plt

# Class Data Set 1 Distance Values
Class_Data = np.array([4.533, 4.65, 4.028, 4.933, 4.416, 4.26, 4.44, 4.525, 4.51, 4.6]) 

# Average Data Set 1 Distance Value
Avg = np.mean(Class_Data)

#Sigma_Avg found through propagation of average formula and distance value's uncertainties
Sigma_Avg = (0.1687)



#Data Set 1 Histogram for class bins
bins = ([4.0, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5.0])
#Plot Histogram Data Set 1
plt.hist(Class_Data, bins=bins, edgecolor='black')


plt.axvline(Avg, color='red', label='Average Data Set 1 Distance Value')
plt.legend()
plt.title ('Class Measurements of Star 1 Distance')
plt.xlabel('Distance (Parsecs)')
plt.ylabel('Number of Groups')