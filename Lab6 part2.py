#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 12:22:54 2022

@author: Wenxi Wu
"""
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
with fits.open('/Users/kristy/Downloads/lab 6/NGC_1832_S_UBVR_k1992.fits') as f:
    NGC1832_i, hdr = fits.getdata('/Users/kristy/Downloads/lab 6/NGC_1832_S_UBVR_k1992.fits', header=True)

    NGC1832 = f[0].data

NGC1832 = NGC1832.T

print(NGC1832)

wavelength = np.linspace(3650,7100,1726)

plt.figure()
plt.title("Intensity vs. Wavelengths")
plt.xlabel("wavelengths (angstrom) ")
plt.ylabel("Normalized Intensity")
plt.plot(wavelength, NGC1832, label = "NGC1832", color = "red")
plt.axvline(3933.7, label = "Ca_K", color = "green")
plt.axvline(3968.5, label = "Ca_H", color = "blue")
plt.axvline(6562.8, label = "Ha")
plt.xlim(6500,7000)
plt.ginput(1)
plt.legend()
