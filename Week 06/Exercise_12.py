# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 10:13:38 2019

@author: thevexis

Exercise_12
MC Method Higher Dimension Integrals

"""

import matplotlib.pyplot as plt
import math as math
import numpy as np
import numpy.random as rand

y = []
x = []
N = 100
summation = []
b = 1   
a = 0

for i in range(N): 
    for l in range(10):
        x = rand.rand(10)*(b-a)
        f = sum(x)
        function = f**2
    summation.append(function)


summation = sum(summation)/N
    
print("10D Integral approximation (with N = 100):", summation)


error = []
x_values = []
N = 0
summation = []
b = 1
a = 0

for l in range(100):
    N += 1
    for i in range(N): 
        for l in range(10):
            x = rand.rand(10)*(b-a)
            f = sum(x)
            function = f**2
        summation.append(function)
    error.append((25.83333 - sum(summation)/N)*100)
    x_values.append(1/(N**(0.5)))
    
    
    
    
plt.plot(x_values,error,'o')
plt.show()

"""
Bigger N gets the smaller the error. It seems that on the graph at the values of
about 0.2 is when the value starts to become accurate. This 0.2 value is equivalent to
N = 400. This computation instead of taking 10^6 years with the brute force method
takes a few seconds with the MC method. It is more efficient to use the MC method when 
the dimensions become greater than 2.

"""

