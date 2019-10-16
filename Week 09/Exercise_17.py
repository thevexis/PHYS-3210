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
import scipy.optimize as opt
from scipy.interpolate import CubicSpline

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

PolyDerivative = np.poly1d.deriv(L)
y_p = Derivative(x)
plt.plot(x,y_p,'r')
plt.show()
print("This is the derivative")
roots = PolyDerivative.r
#using root at 74.58074750
Max = L(74.58074750)
#close to theoretical 78 and very close to np.max(y)


E1 = np.array([0,25,50])
E2 = np.array([75,100,125])
E3 = np.array([150,175,200])
g_E1 = np.array([0,10.6,16.0])
g_E2 = np.array([41.5,83.5,52.8])
g_E3 = np.array([10.8,8.25,4.7])

L1 = lagrange(E1,g_E1)
y1 = L1(x)
plt.plot(x,y1)
plt.show()

L2 = lagrange(E2,g_E2)
y2 = L2(x)
plt.plot(x,y2,'r')
plt.show()

L3 = lagrange(E3,g_E3)
y3 = L3(x)
plt.plot(x,y3,'g')
plt.show()

#From these three we can see the different maximum values for the three peaks 
#The middle one is the largest


#Using CubicSpline technique 

CS = CubicSpline(x,y)
plt.plot(x,CS(x,1),'y')
plt.show()

"""
The cubic spline of CS(x,1) looks like the first derivative 

