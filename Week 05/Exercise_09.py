# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 10:06:21 2019

@author: thevexis

Integration
"""


import matplotlib.pyplot as plt
import math as math
import numpy as np



start = 0
stop = 10 
h = 0.001

x_array = np.arange(start, stop, h)

function_x = x_array**2

plt.plot(x_array, function_x)
plt.show()


def integrate(f, h):
    summation = 0 
    i = 0
    while i < len(f)-1:
        summation += (f[i])*h
        i += 1
    return summation

done = integrate(function_x,h)

        
    