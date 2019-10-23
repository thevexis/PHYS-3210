# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 10:14:43 2019

@author: thevexis

Anharmonic Oscillation with Runge-Kutta 2
Exercise_20
"""


import matplotlib.pyplot as plt
import math as math
import numpy as np 



def RK2(dt,m,p,k):
    
    x = 0.0
    v = 0.1 
    x_array = []
    v_array = []
    t_array = np.arange(0,50,dt)
    
    k1 = dt * v
    
    x = x + dt*(v + (dt/(m*2))*(-k*(x**(p-1))))
    v = v + ((dt/m)*(-k*(x**(p-1))*(v + k1/2)))
    
    
    for t in t_array:
        
        k1 = dt * v
    
        x = x + dt*(v + (dt/(m*2))*(-k*(x**(p-1))))
        v = v + (dt/m)*(-k*(x**(p-1))*(v + k1/2))
        
        x_array.append(x)
        v_array.append(v)
    
    return x_array, v_array, t_array 


x_array, v_array, t_array = RK2(0.1,1,2,1)

plt.plot(t_array,x_array)
plt.title("Position")
plt.show()

plt.plot(t_array,v_array,'r')
plt.title("Velocity")
plt.show()
