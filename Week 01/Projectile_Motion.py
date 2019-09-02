# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 10:16:12 2019

@author: theve
"""

"""
Projectile Motion

"""
mass = float(input("What is the ball's mass in kg: ", ))
x, y, z = input("What is the ball's initial position in terms of x, y, and z (type the value and then a space): ", ).split()
x = float(x)
y = float(y)
z = float(z)
vx, vy, vz = input("What is the ball's initial velocity in terms of velocity_x, velocity_y, and velocity_z (type the value and then a space): ", ).split()
velocity_x = float(vx)
velocity_y = float(vy)
velocity_z = float(vz)
angle = input("What is the launch angle: ", )

delta = 0.01
g = -9.8
t_0 = 0

for t in range(0,100):
    if z == 0:
        break
    x = x + t*delta
    y = y + delta
    z = z + delta
    velocity_x = velocity_x + delta
    velocity_y = velocity_y + delta
    velocity_z = velocity_z + delta
    