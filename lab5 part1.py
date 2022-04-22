#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 11:07:59 2022

@author: Wenxi Wu
"""

import numpy as np
import matplotlib.pyplot as plt

# radius dependent
M_enc = (10**12)*(1.989*10**30)
r = np.linspace(0, 600*(3.086*10**19), 100)
G = 6.67*10**(-11)
R = 600*(3.086*10**19)

def v_orb(r_4,M_r3):
    V = np.sqrt((G*M_r3)/r_4)
    return V

V_orb = v_orb(r,M_enc)

# M proportional to r
M_r = np.linspace(0,M_enc,100)
v = v_orb(r,M_r)

# M proportional to r^3
M_r2 = (r**3)*M_enc*(1/(R**3))
v2 = v_orb(r,M_r2)

plt.figure()
plt.title("Orbital Velocity vs. Radius")
plt.xlabel("orbital radius (m) ")
plt.ylabel("orbital velocity (m/s)")
plt.plot(r, V_orb, label = "radius dependent", color = "red")
plt.plot(r, v, label = "mass proportional to r", color = "blue")
plt.plot(r, v2, label = "mass proportional to r^3", color = "green")
plt.legend()

# step4
r_3 = np.linspace(0,2*(3.086*10**19),100)
R_3 = 2*(3.086*10**19)
M_r3 = (r_3**3)*M_enc*(1/(R_3**3))
v3 = v_orb(r_3,M_r3)
r_4 = np.linspace(2*(3.086*10**19),8*(3.086*10**19),100)

def v_orb4(r_4,M_enc):
    V = np.sqrt((G*M_enc)/r_4)
    return V
v4 = v_orb4(r_4,M_enc)

plt.figure()
plt.title("Orbital Velocity vs. Radius")
plt.xlabel("orbital radius (m) ")
plt.ylabel("orbital velocity (m/s)")
plt.plot(r_3, v3, label = "total enclosed mass", color = "red")
plt.plot(r_4, v4, label = "negligible mass", color = "green")
plt.legend()

