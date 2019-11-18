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
Potential = np.zeros((Xboxmax,Yboxmax),float)
plate_width = 100
plate_initial = 50 #where one side of the plate starts in the x range
plate_final = plate_initial + plate_width #final position of the plate in x range
tolerance = 100
rho = 5*np.ones((Xboxmax,Yboxmax),float) #charge density
delta = 0.01


for k in range(plate_initial,plate_final):
    Potential[k,75] = Plate1
for l in range(plate_initial,plate_final):
    Potential[l,125] = Plate2


for tol in range(tolerance):
    for i in range(1,Xboxmax-2):
        for j in range(1,Yboxmax-2):
            Potential[i,j] = 0.25*(Potential[i+1,j] + Potential[i-1,j] + Potential[i,j+1] + Potential[i,j-1]) + np.pi*(rho[i,j])*(delta**2)        

x = range(0,Xboxmax,1)
y = range(0,Yboxmax,1)

X, Y = np.meshgrid(x,y)

Z = Potential

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(X,Y,Z, cmap=cm.magma)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Potential')
plt.show()















