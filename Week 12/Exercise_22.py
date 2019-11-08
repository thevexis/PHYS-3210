# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 09:58:19 2019

@author: thevexis

Exercise_22
Shooting for an Eigenvalue Solution
"""

import matplotlib.pyplot as plt
import math as math
import numpy as np



E = -10 #MeV
k = -0.0483 * E #MeV^-1 fm^-2



def d2Psi_R(x):
    return (k**2)*np.exp(-k*x)

def d2Psi_L(x):
    return (k**2)*np.exp(k*x)

Xmax = 100
Xmatch = -2
y_0 = 0
y_1 = 0
yR_array = []
xR_array = np.arange(Xmax,Xmatch,-1)

for dx in xR_array:
    y_2R = d2Psi_R(dx) 
    y_1 = dx*y_2R + y_1
    y_0 = -dx*y_1 + y_0
    
    yR_array.append(y_0)
 
plt.plot(xR_array,yR_array)


y_0 = 0
y_1 = 0
Xmax = -100
yL_array = []
xL_array =  np.arange(Xmax,Xmatch,1)

for dx in xL_array:
    y_2L = d2Psi_L(dx) 
    y_1 = dx*y_2L + y_1
    y_0 = -dx*y_1 + y_0
    
    yL_array.append(y_0)

y = yL_array
plt.plot(xL_array,y)
plt.show()



dx = 0.001
x_array = np.arange(-5,5,dx)
Lx_array = np.arange(-5,-2,dx)
Cx_array = np.arange(-2,2,dx)
Rx_array = np.arange(2,5,dx)

Lbox_array = []
box_array = []
Rbox_array = []


for x in x_array:
    if x >= -2 and x <= 2:
        y_2 = (((k/E)*(83))+k**2)*y_0
        y_1 = dx*y_2 + y_1
        y_0 = dx*y_1 + y_0
    
        box_array.append(y_0)
    
    elif x > 2:
        y_2 = (((k/E)*(0))+k**2)*y_0
        y_1 = -dx*y_2 + y_1
        y_0 = dx*y_1 + y_0
    
        Rbox_array.append(y_0)
    
    elif x < -2:
        y_2 = (((k/E)*(0))+k**2)*y_0
        y_1 = dx*y_2 + y_1
        y_0 = dx*y_1 + y_0
    
        Lbox_array.append(y_0)


plt.plot(Lx_array,Lbox_array,'r')
plt.plot(Cx_array,box_array,'b')
plt.plot(Rx_array,Rbox_array,'r')
plt.xlim(-5,5)
plt.show()





