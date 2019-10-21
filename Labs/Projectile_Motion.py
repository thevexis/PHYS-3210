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

def projectile(mass,initial_x,initial_y,velocity,launch_angle):
    theta = launch_angle * (math.pi/180)
    initial_t = 0.0
    dt = 0.01
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

x_position, y_position, time = projectile(1,0,0,5,90)
distance = x_position[np.size(x_position)-1] - x_position[0]
height = np.max(y_position)
plt.plot(x_position,y_position)
plt.show()

print("Time it takes is: ",time)    
print("Distance is: ",distance)
print("Height is: ",height)
    
    