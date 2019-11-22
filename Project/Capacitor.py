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
platey0 = 50 # y initial position of the plate
platey1 = platey0 + plate_width # y final position of plate
tolerance = 1000
delta = 0.1
thickness = 20
platex0 = 75 # x position of the first plate
platex1 = 125 # x position of the second plate
charge_density = 1 #density of charges

Potential = np.zeros((Yboxmax,Xboxmax),float)

rho = np.zeros((Xboxmax,Yboxmax),float) #charge density

for y in range(0,Yboxmax):
    for x in range(0,Xboxmax):
        if y >= platey0 and y <= platey1:
            if x >= platex0 and x <= platex1:
                rho[x,y] = charge_density


for k in range(platey0,platey1):
    Potential[k,platex0] = Plate1

for l in range(platey0,platey1):
    Potential[l,platex1] = Plate2


for tol in range(tolerance):
    for i in range(1,Xboxmax-2):
        for j in range(1,Yboxmax-2):
            Potential[i,j] = 0.25*(Potential[i+1,j] + Potential[i-1,j] + Potential[i,j+1] + Potential[i,j-1]) + np.pi*(rho[i,j])*(delta**2)        

x = range(0,Xboxmax,1)
y = range(0,Yboxmax,1)

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















