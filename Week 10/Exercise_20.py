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



def RK2(dt,m,p,k,x0,v0):
    
    x_array = []
    v_array = []
    t_array = np.arange(0,100,dt)
    
    #Need to fix
    #k1 = dt * f(t,y)
    
    x = x0 + dt*(v0 + (dt/(2))*(-k*(x0**(p-1))))
    v = v0 + ((dt/m)*(-k*((x+(k1/2))**(p-1))))
    
    
    for t in t_array:
        
        k1 = dt * Ex
        x = x + dt*(v + (dt/(2))*(-k*(x**(p-1))))
        v = v + ((dt/m)*(-k*((x+(k1/2))**(p-1))))
        
        
        x_array.append(x)
        v_array.append(v)
    
    return x_array, v_array, t_array 


x_array, v_array, t_array = RK2(0.001,1,2,1,0.1,0.0)

plt.plot(t_array,x_array)
plt.title("Position")
plt.show()

plt.plot(t_array,v_array,'r')
plt.title("Velocity")
plt.show()



#Comparison with Euler Method
def Euler(dt,m,p,k,x0,v0):
    
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

#Comparing p=2
x_array, v_array, t_array = Euler(0.001,1,2,1,0.1,0.0)
x_array2, v_array2, t_array2 = RK2(0.001,1,2,1)

plt.plot(t_array, x_array,'r',label='Euler Method')
plt.plot(t_array2, x_array2, label='Runge Kutta Method')
plt.legend()
plt.show()


Ex = np.asarray(x_array)
Kx = np.asarray(x_array2)
difference = (np.abs(((Ex)**2)-((Kx)**2)))**0.5


