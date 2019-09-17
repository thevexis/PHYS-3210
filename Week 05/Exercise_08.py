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
h = 0.01
x_array = np.arange(start, stop, h)
sine_x_array = np.sin(x_array)

df = np.gradient(sine_x_array,h)


def derivative(f):
    i = 1
    h = 0.01
    while i < len(f):
        df[i] = (f[i] - f[i-1])/h
        i = i + 1
    return df




function = derivative(sine_x_array)

print("This is Cosine:", function)

plt.plot(x_array, function, "r")
plt.show()

print("This is Sine:", sine_x_array)
plt.plot(x_array, df)
plt.show()
