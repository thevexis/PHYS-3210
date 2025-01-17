# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 10:26:34 2019

@author: thevexis
Exercise 19: Anharmonic Oscillation with Euler's method
"""


import matplotlib.pyplot as plt
import math as math
import numpy as np 



"""
Notes:
y_0(t_n+1) = y_0(t) + h * y_1
y_1(t_n+1) = y_1(t) + h/m * (-k*(y_0**p-1))

"""

def Euler(dt,m,p,k):
    
    x = 0.0
    v = 0.1 
    x_array = []
    v_array = []
    t_array = np.arange(0,50,dt)
    
    v = v + (dt/m)*(-k*(x**(p-1)))
    x = x + dt*v
    
    for t in t_array:
        
        v = v + (dt/m)*(-k*(x**(p-1)))
        x = x + dt*v
        
        x_array.append(x)
        v_array.append(v)
    
    return x_array, v_array, t_array 
    

for  n in range(2,12,2):
    x_array, v_array, t_array = Euler(0.1,1,n,1)
    
    plt.plot(t_array,x_array)


plt.show()


for n in range(2,12,2):
    x_array,v_array,t_array = Euler(0.1,1,n,1)
    
    plt.plot(t_array,v_array)


plt.show()
































