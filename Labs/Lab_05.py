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


def EulerFriction(mass,p,k,x0,v0,friction=False,ExternalForce=False):
    
    g = 9.81 #m/s^2
    dt = 0.001
    x_array = []
    v_array = []
    t_array = np.arange(0,100,dt)
    
    if (friction == True and ExternalForce==False):
        
        mu_s = 1.0e-2
        mu_k = 1.0e-2
     
        if abs(v0) < 1.0e-5:
            static  = -mu_s * mass * g 
            kinetic = 0.0  
        else:
            static  = 0.0
            kinetic = -mu_k * mass * g * (v0 / abs(v0))
        
        v = v0 + (dt/mass)*((-k*(x0**(p-1))) + static + kinetic)
        x = x0 + dt*v
        
        for t in t_array:
            
            if abs(v) < 1.0e-5:
                static  = -mu_s * mass * g 
                kinetic = 0.0  
            else:
                static  = 0.0
                kinetic = -mu_k * mass * g * (v / abs(v))
            
            v = v + (dt/mass)*((-k*(x**(p-1))) + static + kinetic)
            x = x + dt*v
            
            
            x_array.append(x)
            v_array.append(v)
            
        return x_array, v_array, t_array
            
    elif (ExternalForce == True and friction==False):
    
        w = (k/mass)**0.5
        
        F0 = 10
        t_initial = 0.0
        Fext = F0*np.sin(w*t_initial)
    
        v = v0 + (dt/mass)*(-k*(x0**(p-1)) + Fext)
        x = x0 + dt*v
        
        for t in t_array:
        
            Fext = F0*np.sin(w*t)
            
            v = v + (dt/mass)*((-k*(x**(p-1))) + Fext)
            x = x + dt*v
                 
            x_array.append(x)
            v_array.append(v)
    
        return x_array, v_array, t_array
                        
    elif (friction == True and ExternalForce == True):
        
        w = (k/mass)**0.5
        mu_s = 1.0e-1
        mu_k = 1.0e-1
        F0 = 10
        t_initial = 0.0
        Fext = F0*np.sin(w*t_initial)
        
        if abs(v0) < 1.0e-5:
            static  = -mu_s * mass * g 
            kinetic = 0.0  
        else:
            static  = 0.0
            kinetic = -mu_k * mass * g * (v0 / abs(v0))

        v = v0 + (dt/mass)*((-k*(x0**(p-1))) + Fext + static + kinetic)
        x = x0 + dt*v
        
        for t in t_array:
            
            Fext = F0*np.sin(w*t)
            
            if abs(v) < 1.0e-5:
                static  = -mu_s * mass * g 
                kinetic = 0.0  
            else:
                static  = 0.0
                kinetic = -mu_k * mass * g * (v / abs(v))
            
            v = v + (dt/mass)*((-k*(x**(p-1))) + Fext + static + kinetic)
            x = x + dt*v
                 
            x_array.append(x)
            v_array.append(v)
    
        return x_array, v_array, t_array
         
    else:

        v = v0 + (dt/mass)*(-k*(x0**(p-1)))
        x = x0 + dt*v
    
        for t in t_array:
            
            v = v + (dt/mass)*(-k*(x**(p-1)))
            x = x + dt*v
        
            x_array.append(x)
            v_array.append(v)
    
        return x_array, v_array, t_array
    

x, v, t = EulerFriction(5,2,10,1.0,0.0,friction=False,ExternalForce=False)
plt.plot(t,x,label='Position')
plt.plot(t,v,'r',label='Velocity')
plt.xlim(0,60)
plt.title('No External Force and  No Friction')
plt.legend()
plt.show()

x, v, t = EulerFriction(5,2,10,1.0,0.0,friction=True,ExternalForce=False)
plt.plot(t,x,label='Position')
plt.xlim(0,60)
plt.plot(t,v,'r',label='Velocity')
plt.title('Friction')
plt.legend()
plt.show()


x, v, t = EulerFriction(5,2,10,1.0,0.0,friction=False,ExternalForce=True)
plt.plot(t,x,label='Position')
plt.plot(t,v,'r',label='Velocity')
plt.xlim(0,60)
plt.title('External Force')
plt.legend()
plt.show()

x, v, t = EulerFriction(5,2,10,1.0,0.0,friction=True,ExternalForce=True)
plt.plot(t,x,label='Position')
plt.plot(t,v,'r',label='Velocity')
plt.xlim(0,60)
plt.title('External Force and Friction')
plt.legend()
plt.show()





















