# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 10:06:21 2019

@author: thevexis

Integration
"""


import matplotlib.pyplot as plt
import math as math
import numpy as np
import scipy.integrate as integrate1

start = 0
stop = 10**4 
h = 0.0001

x_array = np.arange(stop, start, -h)

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

done1 = integrate(function_x,h)

trap = np.trapz(function_x, None, 0.001)
#compare = integrate1.quad(lambda x: function_x, 0, 10)
print("High to Low", done1)
#print(trap)
        

start = 0
stop = 10**4 
h = 0.0001

x_array = np.arange(start, stop, h)

function_x = x_array**2

done2 = integrate(function_x,h)

print("Low to High", done2)

b = 1.0e4
a = 0 
actual = ((b**3)-(a**3))/3
differenceLH = actual - done1
differenceHL = actual - done2
print("Comparison of the difference between low-high to high low")
print("Low to High gives:",differenceLH)
print("High to Low gives:",differenceHL)



