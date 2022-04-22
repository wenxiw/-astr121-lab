#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 12:43:14 2022

@author: Wenxi Wu
"""
import numpy as np
import matplotlib.pyplot as plt

#plots
#lon17
lon17 = np.loadtxt("/Users/kristy/Downloads/Lon-data/lon17.dat")
f_17 = lon17[:,0]
t_17 = lon17[:,1]

plt.figure()
plt.title("Frequency vs. brightness")
plt.xlabel("Frequency (MHz) ")
plt.ylabel("Brightness Temperature (K)")
plt.plot(f_17, t_17, label = "lon17", color = "red")
plt.axvline(x= 1419.73 ,color = "blue", linestyle= "solid",label = "first signal")
plt.legend()

#lon21
lon21 = np.loadtxt("/Users/kristy/Downloads/Lon-data/lon21.dat")
f_21 = lon21[:,0]
t_21 = lon21[:,1]

plt.figure()
plt.title("Frequency vs. brightness")
plt.xlabel("Frequency (MHz) ")
plt.ylabel("Brightness Temperature (K)")
plt.plot(f_21, t_21, label = "lon21", color = "green")
plt.axvline(x= 1419.8 ,color = "blue", linestyle= "solid",label = "first signal")
plt.legend()

#lon25
lon25 = np.loadtxt("/Users/kristy/Downloads/Lon-data/lon25.dat")
f_25 = lon25[:,0]
t_25 = lon25[:,1]

plt.figure()
plt.title("Frequency vs. brightness")
plt.xlabel("Frequency (MHz) ")
plt.ylabel("Brightness Temperature (K)")
plt.plot(f_25, t_25, label = "lon25", color = "purple")
plt.axvline(x= 1419.86 ,color = "blue", linestyle= "solid",label = "first signal")
plt.legend()

#29
lon29 = np.loadtxt("/Users/kristy/Downloads/Lon-data/lon29.dat")
f_29 = lon29[:,0]
t_29 = lon29[:,1]

plt.figure()
plt.title("Frequency vs. brightness")
plt.xlabel("Frequency (MHz) ")
plt.ylabel("Brightness Temperature (K)")
plt.plot(f_29, t_29, label = "lon29", color = "pink")
plt.axvline(x= 1419.86 ,color = "blue", linestyle= "solid",label = "first signal")
plt.legend()

#lon33
lon33 = np.loadtxt("/Users/kristy/Downloads/Lon-data/lon33.dat")
f_33 = lon33[:,0]
t_33 = lon33[:,1]

plt.figure()
plt.title("Frequency vs. brightness")
plt.xlabel("Frequency (MHz) ")
plt.ylabel("Brightness Temperature (K)")
plt.plot(f_33, t_33, label = "lon33", color = "green")
plt.axvline(x= 1419.84 ,color = "blue", linestyle= "solid",label = "first signal")
plt.legend()

#lon37
lon37 = np.loadtxt("/Users/kristy/Downloads/Lon-data/lon37.dat")
f_37 = lon37[:,0]
t_37 = lon37[:,1]

plt.figure()
plt.title("Frequency vs. brightness")
plt.xlabel("Frequency (MHz) ")
plt.ylabel("Brightness Temperature (K)")
plt.plot(f_37, t_37, label = "lon37", color = "brown")
plt.axvline(x= 1419.94 ,color = "blue", linestyle= "solid",label = "first signal")
plt.legend()

#lon41
lon41 = np.loadtxt("/Users/kristy/Downloads/Lon-data/lon41.dat")
f_41 = lon41[:,0]
t_41 = lon41[:,1]

plt.figure()
plt.title("Frequency vs. brightness")
plt.xlabel("Frequency (MHz) ")
plt.ylabel("Brightness Temperature (K)")
plt.plot(f_41, t_41, label = "lon41", color = "black")
plt.axvline(x= 1419.99 ,color = "blue", linestyle= "solid",label = "first signal")
plt.legend()

#lon45
lon45 = np.loadtxt("/Users/kristy/Downloads/Lon-data/lon45.dat")
f_45 = lon45[:,0]
t_45 = lon45[:,1]

plt.figure()
plt.title("Frequency vs. brightness")
plt.xlabel("Frequency (MHz) ")
plt.ylabel("Brightness Temperature (K)")
plt.plot(f_45, t_45, label = "lon45", color = "red")
plt.axvline(x= 1420.03 ,color = "blue", linestyle= "solid",label = "first signal")
plt.legend()

#lon49
lon49 = np.loadtxt("/Users/kristy/Downloads/Lon-data/lon49.dat")
f_49 = lon49[:,0]
t_49 = lon49[:,1]

plt.figure()
plt.title("Frequency vs. brightness")
plt.xlabel("Frequency (MHz) ")
plt.ylabel("Brightness Temperature (K)")
plt.plot(f_49, t_49, label = "lon49", color = "green")
plt.axvline(x= 1420.04 ,color = "blue", linestyle= "solid",label = "first signal")
plt.legend()

#lon53
lon53 = np.loadtxt("/Users/kristy/Downloads/Lon-data/lon53.dat")
f_53 = lon53[:,0]
t_53 = lon53[:,1]

plt.figure()
plt.title("Frequency vs. brightness")
plt.xlabel("Frequency (MHz) ")
plt.ylabel("Brightness Temperature (K)")
plt.plot(f_53, t_53, label = "lon53", color = "green")
plt.axvline(x= 1420.08 ,color = "blue", linestyle= "solid",label = "first signal")
plt.legend()

#lon57
lon57 = np.loadtxt("/Users/kristy/Downloads/Lon-data/lon57.dat")
f_57 = lon57[:,0]
t_57 = lon57[:,1]

plt.figure()
plt.title("Frequency vs. brightness")
plt.xlabel("Frequency (MHz) ")
plt.ylabel("Brightness Temperature (K)")
plt.plot(f_57, t_57, label = "lon57", color = "purple")
plt.axvline(x= 1420.16 ,color = "blue", linestyle= "solid",label = "first signal")
plt.legend()

#lon61
lon61 = np.loadtxt("/Users/kristy/Downloads/Lon-data/lon61.dat")
f_61 = lon61[:,0]
t_61 = lon61[:,1]

plt.figure()
plt.title("Frequency vs. brightness")
plt.xlabel("Frequency (MHz) ")
plt.ylabel("Brightness Temperature (K)")
plt.plot(f_61, t_61, label = "lon61", color = "green")
plt.axvline(x= 1420.21 ,color = "blue", linestyle= "solid",label = "first signal")
plt.legend()

#lon65
lon65 = np.loadtxt("/Users/kristy/Downloads/Lon-data/lon65.dat")
f_65 = lon65[:,0]
t_65 = lon65[:,1]

plt.figure()
plt.title("Frequency vs. brightness")
plt.xlabel("Frequency (MHz) ")
plt.ylabel("Brightness Temperature (K)")
plt.plot(f_65, t_65, label = "lon65", color = "pink")
plt.axvline(x= 1420.24 ,color = "blue", linestyle= "solid",label = "first signal")
plt.legend()

#orbital velocity
f = np.array([1419.73, 1419.80, 1419.86, 1419.86, 1419.84, 1419.94, 1419.99, 1420.03, 1420.04, 1420.08, 1420.16, 1420.21, 1420.24])
f_obs = f*10**6
c = 3*10**8
f_rest = 1420.406*10**6

def v_tan (f_orb):
    v_tan = (c*(f_rest-f_obs))/f_obs
    return v_tan
v_tan = v_tan(f_obs)
print("v_tan", v_tan)
    
v_sun = 254*10**3
theta = np.array([0.297, 0.367, 0.436, 0.506, 0.576, 0.646, 0.716, 0.785, 0.855, 0.925, 0.995, 1.065, 1.134])
v_Los = v_sun * np.sin(theta)

v_orbital = v_tan + v_Los
v_orbital_n = np.append(v_orbital, 254000)
print("v_orbital_n", v_orbital_n)

sigma_v_tan = np.sqrt(((c*f_rest)/(f_obs**2))**2*((0.003*10**6)**2))

print("sigma_v_tan", sigma_v_tan)

sigma_v_Los = np.sqrt((np.sin(theta))**2*((16*10**3)**2))

print("sigma_v_Los", sigma_v_Los)

sigma_v_orbital = np.sqrt((sigma_v_tan**2)+(sigma_v_Los**2))
sigma_v_orbital_n = np.append(sigma_v_orbital, 16000)
print("sigma_v_orbital_n", sigma_v_orbital_n)

#distance
r_sun = 8.4*(3.086*10**19)
r = r_sun * np.sin(theta)
r_n = np.append(r, 8.4*(3.086*10**19))
print("r_n", r_n)

sigma_r = np.sin(theta)*(3.086*10**19)
sigma_r_n = np.append(sigma_r,1.11*10**19)
print("sigma_r_n", sigma_r_n)

#rotational curve
plt.figure()
plt.title("Orbital Velocity vs. Distance")
plt.xlabel("orbital distance (m) ")
plt.ylabel("orbital velocity (m/s)")
plt.plot(r_n, v_orbital_n, color = "green", marker = ".")
plt.errorbar(r_n, v_orbital_n,xerr = sigma_r_n, yerr = sigma_v_orbital_n, fmt = '', ecolor = "orange")

#fitting
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
plt.plot(r_3, v3, label = "theoretical", color = "red")
plt.plot(r_n, v_orbital_n+0.7*(10**6), label = "data", color = "green", marker = ".")
plt.errorbar(r_n, v_orbital_n,xerr = None, yerr = sigma_v_orbital_n, fmt = '', ecolor = "orange")
plt.plot(r_4, v4,color = "red")
plt.legend()







