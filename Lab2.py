#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 17:48:03 2022

@author: Wenxi Wu
"""

import numpy as np
import matplotlib.pyplot as plt

angular_separation = np.array([3.0, 0.2, 0.5, 4, 5, 0.4, 6, 0.2, 4, 0.4])

apparent_distance = np.array([15, 41, 17, 26, 18, 42, 21, 40, 15, 35])
apparent_separation_error = 0.333

plate_scale = np.array([0.0313, 0.0027, 0.0022, 0.0377, 0.357, 0.0048, 0.0667, 0.0020, 0.0625, 0.0033])
plate_scale_error = np.sqrt((-(angular_separation)/apparent_distance**2)**2*((apparent_separation_error)**2))

#parallex angle uncertainty
sigma_p = np.sqrt(((apparent_distance/2)**2)*(plate_scale_error)**2+(plate_scale/2)**2*(apparent_separation_error)**2)

print(sigma_p)
print(plate_scale_error)
print(apparent_separation_error)


#calculating parallex angle
def p(apparent_distance):
    parallax_angle = (apparent_distance * plate_scale)/2
    return parallax_angle

parallax_angle = p(apparent_distance)

print(parallax_angle,sigma_p)

#calculating distance
def d(parallax_angle):
    distance = 1/parallax_angle
    return distance

distance = d(parallax_angle)

sigma_d = np.sqrt(((-1/parallax_angle)**2)*(sigma_p)**2)

print(distance, sigma_d)


#plotting residual

Hipparcos = np.array([4.514, 18.4849, 50.5454, 1.9485, 3.182, 4.953, 1.471, 25.143, 2.394, 17.976])

diff_Hipparcos_measured = np.abs(Hipparcos - distance)
print (diff_Hipparcos_measured)

plt.figure()
plt.scatter(distance, diff_Hipparcos_measured)
plt.title("difference between Hipparcos vs. data")
plt.xlabel("distance")
plt.ylabel("diff_Hipparcos_measured")
plt.errorbar(distance, diff_Hipparcos_measured, yerr = sigma_d, fmt =  ".")






