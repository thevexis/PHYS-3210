# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 07:51:08 2019

@author: thevexis
"""



import math as math
import numpy as np
import matplotlib as plt

    
time = np.linspace(1,10,101)
A = input("Enter a value for constant A: ", )
B = input("Enter a value for constant B: ", )
alpha = input("Enter a value for constant alpha: ", )
beta = input("Enter a value for constant beta: ", )
time

viral_load = A*np.exp((-1)*alpha*time)+ B*np.exp((-1)*beta*time)


plt.plot(time, viral_load)