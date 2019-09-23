# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 10:02:40 2019

@author: thevexis

Exercise_11

Mean-Value Integration 
"""




import matplotlib.pyplot as plt
import math as math
import numpy as np
import scipy.integrate as integrate1
import numpy.random as rand


start = 0
stop = 10 
h = 0.001

x_array = np.arange(start, stop, h)

function_x = x_array**2

x_value = []
y_value = []

def MVI(a,b,N):
    constant = (b - a)/N
    summation = 0 
    for i in range(N):
        x = rand.rand() * b  
        function = x**2 
        summation += function
        x_value.append(x)
        y_value.append(function)
    value = summation * constant
    return value


a=0
b=10
N=10000

for i in range(N):
    x = rand.rand() * b  
    function = x**2 
    x_value.append(x)
    y_value.append(function)


plt.plot(x_value,y_value,'o')
plt.show()



variation = []

for i in range(100):
    v = MVI(0,10,1000)
    variation.append(v)
    
plt.hist(variation)





