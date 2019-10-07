# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 10:05:05 2019

@author: thevexis
Exercise_15
Finding Bound State Energies
"""


import matplotlib.pyplot as plt
import math as math
import numpy as np
import numpy.random as rand
import numpy.linalg as lin 
import scipy.optimize as opt


x_array = np.arange(-20,10,0.01)

c = ((10-x_array)**(1/2))
y = c * np.tan(c) - ((x_array)**(1/2))


def f(x):
    return ((10-x)**(1/2)) * np.tan(((10-x)**(1/2))) - ((x)**(1/2))
    
bisect1 = opt.bisect(f,8,9)

plt.plot(x_array, y,)
plt.ylim(-20,20)
plt.show()

zero_point = opt.newton(f,8)
zero_point2 = opt.newton(f,0)






















