
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 13:45:13 2019

@author: thevexis

Project 
Capacitor
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm




Xboxmax = 200
Yboxmax = 200
Plate1 = 100 #volts
Plate2 = -100
plate_width = 100
tolerance = 1000
delta = 1
thickness = 20
platex0 = 50 # x initial position of the plate
platex1 = platex0 + plate_width  # x final position of plate
platey0 = 75 # y position of the first plate
platey1 = 80 # y position of the second plate
charge_density = 1 #density of charges
plate_distance = 1

x = np.arange(0,Xboxmax,delta)
y = np.arange(0,Yboxmax,delta)

lenx = len(x)
leny = len(y)

Potential = np.zeros((lenx,leny),float)


rho = np.zeros((lenx,leny),float) #charge density
for y in range(0,leny):
    for x in range(0,lenx):
        if y >= (platey0) and y <= (platey1):
            if x >= (platex0) and x <= (platex1):
                rho[x,y] = charge_density


for tol in range(tolerance):
    for i in range(1,lenx-2):
        for j in range(1,leny-2):
            for k in range(0,thickness):
                if i in range(platex0,platex1) and j == platey0:
                    Potential[i-k,platey0] = Plate1
                elif i in range(platex0-plate_distance,platex1-plate_distance) and j == platey1:
                    Potential[i+k,platey1] = Plate2
                else:
                    Potential[i,j] = 0.25*(Potential[i+1,j] + Potential[i-1,j] + Potential[i,j+1] + Potential[i,j-1]) + np.pi*(rho[i,j])*(delta**2)        

x = np.arange(0,Xboxmax,delta)
y = np.arange(0,Yboxmax,delta)

X, Y = np.meshgrid(x,y)

Z = Potential
p = rho

fig = plt.figure()
bx = Axes3D(fig)
bx.plot_surface(X,Y,p, cmap=cm.ocean)
bx.set_xlabel('X')
bx.set_ylabel('Y')
bx.set_zlabel('Charge Density')
plt.show()

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(X,Y,Z, cmap=cm.magma)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Potential')
plt.show()

