# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 09:54:29 2019

@author: thevexis
Lab_05
Ordinary Differential Equations - Non-linear Oscillators 
"""


import matplotlib.pyplot as plt
import math as math
import numpy as np 


def EulerFriction(dt,m,p,k,x0,v0,friction=True):
    
    g = 9.81 #m/s^2
    
    
    if friction == True:
        mu_s = 0.1
        mu_k = 0.1
        
        if abs(v0) < 1.0e-14:
            static  = -mu_s * m * g 
            kinetic = 0.0  
        else:
            static  = -mu_s * m * g 
            kinetic = -mu_k * m * g * (v0 / abs(v0))
        
        x_array = []
        v_array = []
        t_array = np.arange(0,100,dt)
    
        v = v0 + (dt/m)*((-k*(x0**(p-1))) + static + kinetic )
        x = x0 + dt*v
    
        for t in t_array:
            
            if abs(v) < 1.0e-14:
                static  = -mu_s * m * g 
                kinetic = 0.0  
            else:
                static  = -mu_s * m * g 
                kinetic = -mu_k * m * g * (v / abs(v))
            
            v = v + (dt/m)*((-k*(x**(p-1))) + static + kinetic )
            x = x + dt*v
            
            
            x_array.append(x)
            v_array.append(v)
    
        return x_array, v_array, t_array
    
    
    x_array = []
    v_array = []
    t_array = np.arange(0,100,dt)
    
    v = v0 + (dt/m)*(-k*(x0**(p-1)))
    x = x0 + dt*v
    
    for t in t_array:
        
        v = v + (dt/m)*(-k*(x**(p-1)))
        x = x + dt*v
        
        x_array.append(x)
        v_array.append(v)
    
    return x_array, v_array, t_array



x, v, t = EulerFriction(0.01,20,2,1,1.0,0.0,friction=True)
plt.plot(t,x)
plt.xlim(0,60)
plt.show()

plt.plot(t,v,'r')
plt.xlim(0,60)
plt.show()
























