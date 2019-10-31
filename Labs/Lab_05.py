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


def EulerFriction(mass,p,k,x0,v0,friction=True,ExternalForce=True):
    
    g = 9.81 #m/s^2
    dt = 0.1
    x_array = []
    v_array = []
    t_array = np.arange(0,100,dt)
        
    
    if ExternalForce == True:
        F0 = 500
        Fext = F0*np.sin(*t_array)
    else:
        Fext = 0
        
        
    if friction == True:
        mu_s = 1.0e-2
        mu_k = 1.0e-2
        
        if abs(v0) < 1.0e-5:
            static  = -mu_s * mass * g 
            kinetic = 0.0  
        else:
            static  = 0.0
            kinetic = -mu_k * mass * g * (v0 / abs(v0))
        
        v = v0 + (dt/mass)*((-k*(x0**(p-1))) + static + kinetic + Fext )
        x = x0 + dt*v
    
        for t in t_array:
            
            if abs(v) < 1.0e-5:
                static  = -mu_s * mass * g 
                kinetic = 0.0  
            else:
                static  = 0.0
                kinetic = -mu_k * mass * g * (v / abs(v))
            
            v = v + (dt/mass)*((-k*(x**(p-1))) + static + kinetic + Fext )
            x = x + dt*v
            
            
            x_array.append(x)
            v_array.append(v)
            
        return x_array, v_array, t_array
            
    else:
        
        if ExternalForce == True:
            for k in range(0,len(v_array)):
                if v_array[k] < 1.0e-4:
                    F0 = 500
                    Fext = F0*np.sin(t_array[k])
                else:
                    Fext = 0
            x_array = []
            v_array = []
            t_array = np.arange(0,100,dt)
    
             v = v0 + (dt/mass)*(-k*(x0**(p-1)))
             x = x0 + dt*v
    
             for t in t_array:
            
                 v = v + (dt/mass)*(-k*(x**(p-1)) + Fext)
                 x = x + dt*v
                 
                 x_array.append(x)
                 v_array.append(v)
    
             return x_array, v_array, t_array
         
        else:
            Fext = 0
            
         static = 0.0
         kinetic = 0.0
         
         x_array = []
         v_array = []
         t_array = np.arange(0,100,dt)
    
         v = v0 + (dt/mass)*(-k*(x0**(p-1)))
         x = x0 + dt*v
    
         for t in t_array:
            
            v = v + (dt/mass)*(-k*(x**(p-1)) + Fext)
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
        
        v = v + (dt/m)*(-k*(x**(p-1)) + Fext)
        x = x + dt*v
        
        x_array.append(x)
        v_array.append(v)
    
    return x_array, v_array, t_array



x, v, t = EulerFriction(5,2,10,1.0,0.0,friction=True,ExternalForce=False)
plt.plot(t,x,label='Position')
plt.xlim(0,60)
plt.plot(t,v,'r',label='Velocity')
plt.legend()
plt.show()

"""
x, v, t = EulerFriction(5,2,10,1.0,0.0,friction=False,ExternalForce=True)
plt.plot(t,x)
plt.xlim(0,60)
plt.show()

plt.plot(t,v,'r')
plt.xlim(0,60)
plt.show()
"""





















