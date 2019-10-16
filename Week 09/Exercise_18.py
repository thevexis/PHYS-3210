# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 10:17:36 2019

@author: thevexis

Exercise_18
Pi Meson Lifetime
"""


import matplotlib.pyplot as plt
import math as math
import numpy as np 
import numpy.linalg as lin 
from scipy.optimize import curve_fit


data = np.loadtxt('pi_meson_decays.dat')


def f(t,l,N_0):
    return N_0 * np.exp(-t*l)

x_array = np.arange(5,120,0.1)
function = f(x_array,1,1000)

plt.plot(x_array,function)
plt.xlim(0,20)
plt.show()

xdata = data[:,0]
ydata = data[:,1]

plt.plot(xdata,ydata,'o')
plt.show()

l=1
N_0 = 1000

popt, popc = curve_fit(f,xdata,ydata)






















