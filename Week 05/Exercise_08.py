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
h = 0.0001
x_array = np.arange(start, stop, h)
sine_x_array = np.sin(x_array)

df = np.gradient(sine_x_array,h)


def derivative(f,h):
    i = 0
    df = []
    while i < len(f)-1:
        df.append((f[i+1] - f[i])/h)
        i += 1
    return df




function = derivative(sine_x_array,h)

x = x_array[:-1]

#print("This is Cosine:", function)

plt.plot(x, function, "r")
plt.show()

print("This is Sine:", sine_x_array)
plt.plot(x_array, sine_x_array)
plt.show()


plt.plot(x, function, "r")
plt.plot(x_array, sine_x_array )
plt.show()


#Graph of numpys gradient and mine are so close to the same you do not see a difference on the graph
plt.plot(x, function, "r")
plt.plot(x_array, df )
plt.show()

#second derivative with np gradient function
df2 = np.gradient(df,h)
plt.plot(x_array, df2, "g")
plt.show()

x = x[:-1]
#second derivative
function2 = derivative(function,h)
plt.plot(x, function2)
plt.show()