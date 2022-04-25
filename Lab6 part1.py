#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 11:28:42 2022

@author: Wenxi Wu
"""
import numpy as np
import pandas as pd

#read in distance data
NGC1832D = pd.read_csv("/Users/kristy/Downloads/lab 6/NGC1832.csv")
NGC1832d = NGC1832D['D(Mpc)']
NGC1832d_avg = np.mean(NGC1832d)
NGC1832d_sigma = np.std(NGC1832d)/(np.sqrt(27))
print("1832:", NGC1832d_avg)
print(NGC1832d_sigma)

NGC2276D = pd.read_csv("/Users/kristy/Downloads/lab 6/NGC2276.csv")
NGC2276d = NGC2276D['D(Mpc)']
NGC2276d_avg = np.mean(NGC2276d)
NGC2276d_sigma = np.std(NGC2276d)/(np.sqrt(10))
print("2276: ", NGC2276d_avg)
print(NGC2276d_sigma)

NGC2798D = pd.read_csv("/Users/kristy/Downloads/lab 6/NGC2798.csv")
NGC2798d = NGC2798D['D(Mpc)']
NGC2798d_avg = np.mean(NGC2798d)
NGC2798d_sigma = np.std(NGC2798d)/(np.sqrt(10))
print("2798: ", NGC2798d_avg)
print(NGC2798d_sigma)

NGC2903D = pd.read_csv("/Users/kristy/Downloads/lab 6/NGC2903.csv")
NGC2903d = NGC2903D['D(Mpc)']
NGC2903d_avg = np.mean(NGC2903d)
NGC2903d_sigma = np.std(NGC2903d)/(np.sqrt(28))
print("2903: ", NGC2903d_avg)
print(NGC2903d_sigma)

NGC3034D = pd.read_csv("/Users/kristy/Downloads/lab 6/NGC3034.csv")
NGC3034d = NGC3034D['D(Mpc)']
NGC3034d_avg = np.mean(NGC3034d)
NGC3034d_sigma = np.std(NGC3034d)/(np.sqrt(21))
print("3034: ", NGC3034d_avg)
print(NGC3034d_sigma)

NGC3147D = pd.read_csv("/Users/kristy/Downloads/lab 6/NGC3147.csv")
NGC3147d = NGC3147D['D(Mpc)']
NGC3147d_avg = np.mean(NGC3147d)
NGC3147d_sigma = np.std(NGC3147d)/(np.sqrt(16))
print("3147: ", NGC3147d_avg)
print(NGC3147d_sigma)

NGC3368D = pd.read_csv("/Users/kristy/Downloads/lab 6/NGC3368.csv")
NGC3368d = NGC3368D['D(Mpc)']
NGC3368d_avg = np.mean(NGC3368d)
NGC3368d_sigma = np.std(NGC3368d)/(np.sqrt(71))
print("3368: ", NGC3368d_avg)
print(NGC3368d_sigma)

NGC3627D = pd.read_csv("/Users/kristy/Downloads/lab 6/NGC3627.csv")
NGC3627d = NGC3627D['D(Mpc)']
NGC3627d_avg = np.mean(NGC3627d)
NGC3627d_sigma = np.std(NGC3627d)/(np.sqrt(79))
print("3627: ", NGC3627d_avg)
print(NGC3627d_sigma)

#sigma undecided
NGC4750D = pd.read_csv("/Users/kristy/Downloads/lab 6/NGC4750.csv")
NGC4750d = NGC4750D['D(Mpc)']
NGC4750d_avg = np.mean(NGC4750d)
NGC4750d_sigma = 0.5
print("4750 ", NGC4750d_avg)
print(NGC4750d_sigma)

NGC4775D = pd.read_csv("/Users/kristy/Downloads/lab 6/NGC4775.csv")
NGC4775d = NGC4775D['D(Mpc)']
NGC4775d_avg = np.mean(NGC4775d)
NGC4775d_sigma = np.std(NGC4775d)/(np.sqrt(4))
print("4775: ", NGC4775d_avg)
print(NGC4775d_sigma)

NGC5195D = pd.read_csv("/Users/kristy/Downloads/lab 6/NGC5195.csv")
NGC5195d = NGC5195D['D(Mpc)']
NGC5195d_avg = np.mean(NGC5195d)
NGC5195d_sigma = np.std(NGC5195d)/(np.sqrt(51))
print("5195: ", NGC5195d_avg)
print(NGC5195d_sigma)

NGC5248D = pd.read_csv("/Users/kristy/Downloads/lab 6/NGC5248.csv")
NGC5248d = NGC5248D['D(Mpc)']
NGC5248d_avg = np.mean(NGC5248d)
NGC5248d_sigma = np.std(NGC5248d)/(np.sqrt(18))
print("5248: ", NGC5248d_avg)
print(NGC5248d_sigma)

NGC6181D = pd.read_csv("/Users/kristy/Downloads/lab 6/NGC6181.csv")
NGC6181d = NGC6181D['D(Mpc)']
NGC6181d_avg = np.mean(NGC6181d)
NGC6181d_sigma = np.std(NGC6181d)/(np.sqrt(28))
print("6181: ", NGC6181d_avg)
print(NGC6181d_sigma)

NGC6643D = pd.read_csv("/Users/kristy/Downloads/lab 6/NGC6643.csv")
NGC6643d = NGC6643D['D(Mpc)']
NGC6643d_avg = np.mean(NGC6643d)
NGC6643d_sigma = np.std(NGC6643d)/(np.sqrt(25))
print("6643: ", NGC6643d_avg)
print(NGC6643d_sigma)




