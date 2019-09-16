# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 10:08:54 2019

@author: thevexis

Exercise_08
"""

import matplotlib.pyplot as plt
import math as math
import numpy as np

start = -2*math.pi
stop = 2*math.pi + 0.000000001
h = 0.001
x_array = np.arange(start, stop, h)
sine_x_array = np.sin(x_array)

df = np.gradient(sine_x_array,h)


def derivative(f):
    h = 0.001
    for n in range(0,(len(f)-1)):
        difference = f[n+1]
        df = [(difference - f[n])/(h)]
    return df[n-1] 


function = derivative(sine_x_array)

plt.plot(x_array, function)
plt.plot(x_array, df)
plt.show()
