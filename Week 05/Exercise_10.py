# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 10:06:23 2019

@author: thevexis

Exercise 10:
Monte Carlo Integration

"""

import matplotlib.pyplot as plt
import math as math
import numpy as np
import numpy.random as rand


N = 10000000


pos_x = rand.rand(N)
x = (pos_x - 0.5 )*2


pos_y = rand.rand(N)
y = (pos_y - 0.5)*2




plt.plot(x,y,'o')
plt.show()

i = 0 
N_pond = 0
distance = []
Pond = []


while i < N:
    distance.append((x[i]**2 + y[i]**2)**(0.5))
    if distance[i] <= 1:
        Pond.append((x[i]**2 + y[i]**2)**(0.5))
        N_pond += 1
    i += 1 
    
Circle_over_Square = N_pond/N
Area_Square = 4
Area_Pond = 4 * Circle_over_Square
print(Area_Pond)

plt.plot(x,y,'o')
plt.plot(Pond, 'o','r')
plt.show()




















