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

error = np.sqrt(ydata)
errors = np.array([ 5.65685425,  4.24264069,  4.58257569,  2.82842712,  3.        ,
        2.64575131,  2.44948974,  1.73205081,  2.        ,  1.        ,
        2.23606798,  1.        ])

plt.plot(xdata,ydata,'o')
plt.show()


#to remove errors with log(0)
ydata1 = np.array([32.,18.,21.,8.,9.,7.,6.,3.,4.,0.0,5.,1.])
liny = np.log(ydata1)


def g(t,l,N_0):
    return -l*t + np.log(N_0)

p, c = curve_fit(g,xdata,ydata1,sigma=errors)

initial_N = p[1]
l = p[0]

tau = l**-1

plt.plot(xdata,liny,'o')
fitted_line = g(x_array,l,initial_N)
plt.plot(x_array,fitted_line)
plt.show()


l=1
N_0 = 1000

parameters, covm = curve_fit(f,xdata,ydata,sigma=errors)

l = parameters[0]
N_0 = parameters[1]

fitted_curve = f(x_array,l,N_0)
plt.plot(x_array,fitted_curve)
plt.plot(xdata,ydata,'o')
plt.show()


Tau = l**-1
#percent_error_pi_meson_lifetime
percent_error = ((((Tau/10) - 2.6)/(2.6)) * 100) 

"""
Tau which is the lifetime of the pi-meson, comes out to be 32.6 * 10**-9 since each
step delta-t was in terms of nanoseconds. The tabulated lifetime for a pi-meson is 2.6 * 10**-8
which gives about 19.04 percent error. 

"""


















