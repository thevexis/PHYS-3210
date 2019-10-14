# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 10:03:51 2019

@author: thevexis

Exercise_16
Temperature Dependence of Magnetization
"""

import matplotlib.pyplot as plt
import math as math
import numpy as np
import numpy.random as rand
import numpy.linalg as lin 
import scipy.optimize as opt




def f(m,t):
    return m - np.tanh(m/t)

m = np.arange(-10,10,0.01)

t = np.arange(-2,3,0.5) 

for i in range(len(t)):
    x = t[i]
    y = f(m,x)
    plt.plot(m,y)

plt.ylim(-2,2)
plt.xlim(-2,2)
plt.show()
print("Many Graphs")




def g(m):
    return m - np.tanh(2*m)

y = g(m)
plt.plot(m,y)
plt.ylim(-2,2)
plt.xlim(-2,2)
plt.show()


zeros = opt.newton(g,1,tol=0.000001)
print("Newton-Raphson Method:",zeros)

zeroB = opt.bisect(g,0.5,1.5,xtol=0.000001)
print("Bisection Method:",zeroB)


t = 0.5*np.ones(2000)

plt.plot(y,t)
plt.show()


#for t>=1
def n(m):
    return m - np.tanh((0.5)*m)

y2 = n(m)
plt.plot(m,y2)
plt.show()
zero2 = opt.newton(n,1)

"""
At this point we only have zeros at zero and no longer have zeros at any m value.

When we look at the seafloor we find stripped patterns where one section of the floor
is oriented either north or south and its neighbor is oriented the other direction. 
This shows that new layers of the seafloor are spreading out from a certain point and that
because of their orientation the magnetic field of the earth was in that direction at that
time in history. 
"""





