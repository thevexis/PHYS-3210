# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 10:10:20 2019

@author: thevexis
Exercise_17
Fitting an Energy Spectrum with Lagrange Interpolation
"""


import matplotlib.pyplot as plt
import math as math
import numpy as np 
from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial
import numpy.linalg as lin 


E = np.arange(0,225,25)
g_E = np.array([10.6,16.0,45.0,83.5,52.8,19.9,10.8,8.25,4.7])
error = np.array([9.34,17.9,41.5,85.5,51.5,21.5,10.8,6.29,4.14])

plt.plot(E,g_E,'o','r')
plt.xlabel("Energy")
plt.ylabel("Function of Energy")
plt.show()

L = lagrange(E,g_E)


x = np.arange(0,201,1)
y = L(x)
plt.plot(x,y)
plt.show()

Maximum = np.max(y)

Derivative = np.poly1d.deriv(L)
y_p = Derivative(x)
plt.plot(x,y_p,'r')
plt.show()

E1 = np.array([0,25,50])
E2 = np.array([75,100,125])
E3 = np.array([150,175,200])
g_E1 = np.array([0,10.6,16.0])
g_E2 = np.array([41.5,83,5,52.8])
g_E3 = np.array([10.8,8,25,4.7])

L1 = lagrange(E1,g_E1)
y1 = L1(x)
plt.plot(x,y1)
plt.show()

L1 = lagrange(E2,g_E2)
y2 = L1(x)
plt.plot(x,y2)
plt.show()