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
plate_width = 1000
tolerance = 100
delta = 0.1
thickness = 20
platey0 = 500 # y initial position of the plate
platey1 = platey0 + plate_width  # y final position of plate
platex0 = 750 # x position of the first plate
platex1 = 800 # x position of the second plate
charge_density = 1 #density of charges

x = np.arange(0,Xboxmax,delta)
y = np.arange(0,Yboxmax,delta)

lenx = len(x)
leny = len(y)

Potential = np.zeros((lenx,leny),float)


rho = np.zeros((lenx,leny),float) #charge density
for y in range(0,leny):
    for x in range(0,lenx):
        if y >= (platey0*(delta**-1)) and y <= (platey1*(delta**-1)):
            if x >= (platex0*(delta**-1)) and x <= (platex1*(delta**-1)):
                rho[x,y] = charge_density


for k in range(platey0,platey1):
    Potential[k,platex0] = Plate1

for l in range(platey0-1,platey1-1):
    Potential[l,platex1] = Plate2


for tol in range(tolerance):
    for i in range(1,lenx-2):
        for j in range(1,leny-2):
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















