# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 10:16:12 2019

@author: theve
"""

"""
Projectile Motion

"""

import matplotlib.pyplot as plt
import math as math
import numpy as np 

def projectile(initial_x,initial_y,velocity,launch_angle):
    theta = launch_angle * (math.pi/180)
    initial_t = 0.0
    dt = 0.0001
    g = -9.8
    x_position = []
    y_position = []
    
    t_array = np.arange(0,10,dt)
    for t in t_array:
        x = initial_x + velocity*t*(np.cos(theta))
        y = initial_y + velocity*t*(np.sin(theta)) + 0.5*g*(t**2) 
    
        x_position.append(x)
        y_position.append(y)    
        initial_t += dt
        
        if y < 0:
            break
    return x_position, y_position, initial_t

x_position, y_position, time = projectile(0,0,5,45)
distance = x_position[np.size(x_position)-1] - x_position[0]
height = np.max(y_position)
plt.plot(x_position,y_position)
plt.legend("N")
plt.show()

print("This is a projectile without air resistance")
print("Time it takes is:",time, "seconds")    
print("Distance is:",distance, "meters")
print("Height is:",height, "meters")
    
"""
With air resistance the projectile should go a shorter distance, have less height, and
take more time. 

"""


#not currently correct
def projectile_drag(mass,initial_x,initial_y,velocity,launch_angle):
    theta = launch_angle * (math.pi/180)
    initial_t = 0.0
    dt = 0.01
    g = -9.8
    c = 2 * 10**-3
    x_position = []
    y_position = []
    force_air = c * (velocity**2)
    
    t_array = np.arange(0,10,dt)
    for t in t_array:
        x = initial_x + velocity*t*(np.cos(theta)) - 0.5/mass*force_air*(t**2)
        y = initial_y + velocity*t*(np.sin(theta)) + 0.5*(g-force_air/mass)*(t**2) 
    
        x_position.append(x)
        y_position.append(y)    
        initial_t += dt
        
        if y < 0:
            break
    return x_position, y_position, initial_t
    
x_position, y_position, time = projectile_drag(1,0,0,5,45)
distance = x_position[np.size(x_position)-1] - x_position[0]
height = np.max(y_position)
plt.plot(x_position,y_position,'r')
plt.legend("D")
plt.show()


#Not currently working
print("This is a projectile with air resistance")
print("Time it takes is:",time, "seconds")    
print("Distance is:",distance, "meters")
print("Height is:",height, "meters")