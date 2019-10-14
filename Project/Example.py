# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 11:41:42 2019

@author: thevexis

Project
Partial Differential Equations 
"""


import matplotlib.pylab as p;
from mpl_toolkits.mplot3d import Axes3D
from numpy import *;
import numpy;

print("Initializing")
Nmax = 50; Niter = 70; V=zeros((Nmax,Nmax),float)

for k in range(0,Nmax-1): V[0,k]=100
for iter in range(Niter):
    if iter%10 == 0: print(iter)
    for i in range(1,Nmax-2):
        for j in range(1,Nmax-2):
            V[i,j]=0.25*(V[i+1,j]+V[i-1,j]+V[i,j+1]+V[i,j-1])
x = range(0,Nmax-1,2); y=range(0,50,2)
X, Y = p.meshgrid(x,y)

def functz(V):
    z = V[X,Y]
    return z

Z = functz(V)
fig = p.figure()
ax = Axes3D(fig)
ax.plot_wireframe(X,Y,Z, color='r')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Potential')
p.show()



