# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 10:16:12 2019

@author: theve
"""

"""
Projectile Motion

"""

import matplotlib.pyplot as plt
import numpy as np 


def projectile(mass,initial_x,initial_y,velocity_initial,launch_angle):
    theta = launch_angle * (math.pi/180)
    dt = 0.0001
    g = -9.8
    x = []
    y = []
    
    vx = velocity_initial*(np.cos(theta))
    vy = velocity_initial*(np.sin(theta))
    
    X_2 = 0
    X_1 = dt * X_2 + vx
    X_0 = dt * X_1 + initial_x
    Y_2 = g/mass + 0
    Y_1 = dt * Y_2 + vy
    Y_0 = dt * Y_1 + initial_y
    
    t_array = np.arange(0,10,dt)
    
    for t in t_array:
    
        X_2 = 0
        X_1 = dt * X_2 + X_1
        X_0 = dt * X_1 + X_0
        Y_2 = g/mass + 0
        Y_1 = dt * Y_2 + Y_1
        Y_0 = dt * Y_1 + Y_0
        
        x.append(X_0)
        y.append(Y_0)    
        
        if Y_0 < 0.0:
            break
        
    return x, y, t_array, t

x_position, y_position, time, time_end = projectile(1,0,0,50,45)
distance = x_position[np.size(x_position)-1] - x_position[0]
height = np.max(y_position)
plt.plot(x_position,y_position,label='No Drag')




"""
With air resistance the projectile should go a shorter distance, have less height, and
take more time. 

"""
#not currently correct
def projectile_drag(mass,initial_x,initial_y,velocity_initial,launch_angle):
    theta = launch_angle * (math.pi/180)
    dt = 0.001
    g = -9.8
    c = 2 * 10**-3
    x = []
    y = []
     
    vx = velocity_initial*(np.cos(theta))
    vy = velocity_initial*(np.sin(theta))
    
    X_2 = -(c/mass)*(vx/abs(vx))*(vx**2)
    X_1 = dt * X_2 + vx
    X_0 = dt * X_1 + initial_x
    Y_2 = g/mass - (c/mass)*(vy/abs(vy))*(vy**2)
    Y_1 = dt * Y_2 + vy
    Y_0 = dt * Y_1 + initial_y
    
    
    t_array = np.arange(0,10,dt)
    
    for t in t_array:
        
        X_2 = -(c/mass)*(X_1/abs(X_1))*(X_1**2)
        X_1 = dt * X_2 + X_1
        X_0 = dt * X_1 + X_0
        Y_2 = g/mass - (c/mass)*(Y_1/abs(Y_1))*(Y_1**2)
        Y_1 = dt * Y_2 + Y_1
        Y_0 = dt * Y_1 + Y_0
    
        x.append(X_0)
        y.append(Y_0)    
        
        if Y_0 < 0.0:
            break
        
    return x, y, t_array, t
    
x_position, y_position, time, time_end1 = projectile_drag(1,0,0,50,45)
distance1 = x_position[np.size(x_position)-1] - x_position[0]
height1 = np.max(y_position)
plt.plot(x_position,y_position,'r',label='Drag')
plt.legend()

plt.show()

print('In blue is a projectile without air resistance')
print("Time it takes is:",time_end, "seconds")    
print("Distance is:",distance, "meters")
print("Height is:",height, "meters")

print(end='\n')

print('In red is a projectile with air resistance')
print("Time it takes is:",time_end1, "seconds")    
print("Distance is:",distance1, "meters")
print("Height is:",height1, "meters")


