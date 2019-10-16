# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 10:16:12 2019

@author: theve
"""

"""
Projectile Motion

"""
mass = float(input("What is the ball's mass in kg: ", ))
x, y = input("What is the ball's initial position in terms of x, and y (type the value and then a space): ", ).split()
x_0 = float(x)
y_0 = float(y)
vx, vy = input("What is the ball's initial velocity in terms of velocity_x, and velocity_y (type the value and then a space): ", ).split()
velocity_x_0 = float(vx)
velocity_y_0 = float(vy)
angle = input("What is the launch angle in degrees: ", )
angle = float(angle)
theta = math.pi * angle / 180

delta = 0.1
g = 9.8
t_0 = 0
drag = 0

for n in range(1,1000):
    
    t = t_0 + n*delta
    
    if t >= 2*math.sin(theta)/g:
        break
    
    x = x_0 + n*delta
    y = y_0 + n*delta
    
    velocity_x = (velocity_x_0 + n*delta)*math.cos(theta)*t
    velocity_y = (velocity_y_0 + n*delta)*math.sin(theta)*t
   
    y_final = y_0 + velocity_y_0*math.sin(theta)*t - (0.5)*g*(t**2)
    
    x_final = x_0 + velocity_x_0*math.cos(theta)*t - drag*(velocity_x**2) 

print("The y final position is ", y_final, "m") 
print("The x final position is ", x_final, "m")
print("The y final velocity is ", velocity_y, "m/s")
print("The x final velocity is ", velocity_x, "m/s")

    
    
    
    
    