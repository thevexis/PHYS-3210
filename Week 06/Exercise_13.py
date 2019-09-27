# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 09:58:54 2019

@author: thevexis

Exercise_13
Acceptance & Rejection Methods

"""







import matplotlib.pyplot as plt
import math as math
import numpy as np
import numpy.random as rand


x = []
y = []
x1 = []
function_x = []
square = []

for i in range(1000):
    plain = rand.rand(2)
    x_values = plain[0]*10
    y_values = plain[1]*100
    x.append(x_values)
    y.append(y_values)
    functionx = (x_values)**2
    square.append(x_values**2) 
    function_x.append(functionx)
    if y[i] < function_x[i]:
        function_x.append(y[i])

change = len(function_x) - len(y)
y2 = function_x[:-change]
    
plt.plot(x,y,'o')
plt.plot(x,square,'o')
#plt.plot(x,y2,'o')


    
plt.show()







