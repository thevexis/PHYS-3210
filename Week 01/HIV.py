# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 07:51:08 2019
Created on Fri Aug 30 09:55:03 2019

@author: thevexis

We make the assumptions of knowing some constant values
the original equation in the text is equal to N(t) =  X*e^(-k_I*t)+(N_V0 - X)*e^(-k_v*t)
where X was a constant value equal to beta/(k_V-k_I), where k_I is the clearence rate constant
for infected T cells, k_V is the clearence rate for virions, beta is equal to gamma*N_I0, where gamma 
is the rate constant for virion production per infected T cell and N_I0 is the intial population of 
infected T cells.

We also made some assumptions in the derivation of our differential equation.
Instead of solving equation 1.3 intuitions were made based on if k_I >> k_V and 
k_V >> k_I in which it was assumed that the long term equation is proportional either
to e^(-k_V*t) or e^(-k_I*t) in which the trial function N(t) was formed.

If we did not make these assumptions then we would most likely have a partial differential
equation that we would have to solve with an infinite sum so our script could not have used
an easy exponential function instead we would have to do many summations of linear fucntions with many constants 
and use that as our equation for python to solve which would take more time and computing power


"""




import math as math
import numpy as np
import matplotlib.pyplot as plt

HIV_data = np.loadtxt("C:/Users/theve/Documents/GitHub/PHYS-3210/Week 01/data/HIVseries.csv")

    
time = np.linspace(1,10,101)

"""

A = float(input("Enter a value for constant A: ", ))
B = float(input("Enter a value for constant B: ", ))
alpha = float(input("Enter a value for constant alpha: ", ))
beta = float(input("Enter a value for constant beta: ", ))

"""

fig = plt.figure()
ax = fig.add_subplot(111)

for A in range(0,5):
    
    B = 1
    alpha = 1
    beta = 1
    
    viral_load = A*np.exp((-1)*alpha*time)+ B*np.exp((-1)*beta*time)
    x_points = viral_load
    y_points = time
    p = ax.plot(x_points, y_points, 'o', c='r')
    
p = ax.plot(x_points, y_points, 'o', c='r', label="A")
    
    
   
for B in range(0,5):
    
    A = 1
    alpha = 1
    beta = 1
    
    viral_load = A*np.exp((-1)*alpha*time)+ B*np.exp((-1)*beta*time)
    x_points = viral_load
    y_points = time
    p = ax.plot(x_points, y_points, '-', c='g')
    
p = ax.plot(x_points, y_points, '-', c='g', label="B")
    
    

for alpha in range(0,5):
    
    A = 1
    B = 1
    beta = 1
    
    viral_load = A*np.exp((-1)*alpha*time)+ B*np.exp((-1)*beta*time)
    x_points = viral_load
    y_points = time
    p = ax.plot(x_points, y_points, 'o', c='c')
    
p = ax.plot(x_points, y_points, 'o', c='c', label="alpha")
    
    

for beta in range(0,5):
    
    A = 1
    B = 1
    alpha = 1
    
    viral_load = A*np.exp((-1)*alpha*time)+ B*np.exp((-1)*beta*time)
    x_points = viral_load
    y_points = time
    p = ax.plot(x_points, y_points, '-', c='b')
    
p = ax.plot(x_points, y_points, '-', c='b', label="beta")
    
    
ax.set_xlabel('Viral Load')
ax.set_ylabel('Time')
ax.set_title('HIV Graph')
ax.legend(loc='upper right')
fig.show()
plt.savefig("HIV.pdf")


#plt.plot(time, viral_load)

