# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 10:02:44 2019

@author: thevexis
Exercise 23
Coupled Ordinary Differential Equations

"""

import numpy as np
import matplotlib.pyplot as plt



def Pinball(mass,InitialY,InitialX,IntVelocityY,IntVelocityX):
    
    start = 0
    stop = 5000
    dt = 0.01
    time = np.arange(start,stop,dt)
    
    
    ax = [] 
    ay = [] 
    x = []
    y = []
    vx = []
    vy = []
    
    X_2 = -(1/mass)*2*(InitialX)*(InitialY**2)*np.exp(-(InitialX**2)-(InitialY**2))*(1-InitialX**2)
    X_1 = dt * X_2 + IntVelocityX
    X_0 = dt * X_1 + InitialX

    Y_2 = -(1/mass)*2*(InitialY)*(InitialX**2)*np.exp(-(InitialX**2)-(InitialY**2))*(1-InitialY**2)
    Y_1 = dt * Y_2 + IntVelocityY
    Y_0 = dt * Y_1 + InitialY    
    
    
    
    for t in time:
    
        X_2 = -(1/mass)*2*(X_0)*(Y_0**2)*np.exp(-(X_0**2)-(Y_0**2))*(1-X_0**2)
        X_1 = dt * X_2 + X_1
        X_0 = dt * X_1 + X_0
    
        Y_2 = -(1/mass)*2*(Y_0)*(X_0**2)*np.exp(-(X_0**2)-(Y_0**2))*(1-Y_0**2)
        Y_1 = dt * Y_2 + Y_1
        Y_0 = dt * Y_1 + Y_0
        
        Px.append(X_2)
        Py.append(Y_2)
        x.append(X_0)
        y.append(Y_0)
        vx.append(X_1)
        vy.append(Y_1)
        
        
    count = 0
    for l in range(0,len(vx)-1):
        if np.sign(vx[l]) != np.sign(vx[l+1]):
            count += 1
        if np.sign(vy[l]) != np.sign(vy[l+1]):
            count += 1
            
    
    return x, y, vx, vy, count, Px, Py



x ,y , vx, vy, countB, Px, Py = Pinball(0.1,-0.2,-0.8,0.001,0.5)
x1, y1, vx1, vy1, countO, Px1, Py1 = Pinball(0.1,0,0.94,0.005,-0.0001)

x_v = np.arange(-10.0, 10.01, 0.01)
y_v = np.arange(-10.0, 10.01, 0.01)
X_v, Y_v = np.meshgrid(x_v, y_v)
Z_v = X_v**2 * Y_v**2 * np.exp(-(X_v**2 + Y_v**2))

fig, ax = plt.subplots(1, 1, figsize=(10, 8))

cb = ax.contourf(X_v, Y_v, Z_v, 20, cmap="Purples")
ax.plot(x,y, lw=2)
ax.plot(x1,y1, lw=2)

ax.set_xlim(-3.0, 3.0)
ax.set_xlabel("X Position")
ax.set_ylim(-3.0, 3.0)
ax.set_ylabel("Y Position")

cbar = fig.colorbar(cb)
cbar.ax.set_ylabel("Scattering Potential")

fig.tight_layout()
plt.savefig('Bouncing')

plt.show()


print("The number of bounces of the orange particle is:", countO)

plt.plot(Px,Py)
plt.show()



