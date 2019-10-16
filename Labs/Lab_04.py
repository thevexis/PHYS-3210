# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 10:38:07 2019

@author: thevexis

Lab_04
Masses on a String
"""

import matplotlib.pyplot as plt
import math as math
import numpy as np
import numpy.random as rand
import numpy.linalg as lin 


#Guesses
guess = np.array(([0.5],[0.5],[0.5],[0.5],[0.5],[0.5],[8],[8],[12]))
x1 = guess[0]
x2 = guess[1]
x3 = guess[2]
x4 = guess[3]
x5 = guess[4]
x6 = guess[5]
x7 = guess[6]
x8 = guess[7]
x9 = guess[8]

zero = np.array(([0],[0],[0],[0],[0],[0],[0],[0],[0]))

delta_x = []

f = np.array([3*x4 + 4*x5 + 4*x6 - 8,3*x1 + 4*x2 - 4*x3,x7*x1 - x8*x2 - 10,x7*x4 - x8*x5,x8*x2 + x9*x3 - 20,x8*x5 - x9*x6,x1**2 + x4**2 - 1, x2**2 + x5**2 - 1,x3**2 + x6**2 - 1])
f = np.reshape(f,(9,1))
J = np.array(([0,0,0,3,4,4,0,0,0],[3,4,-4,0,0,0,0,0,0],[x7,-x8,0,0,0,0,x1,-x2,0],[0,0,0,x7,-x8,0,x4,-x5,0],[0,x8,x9,0,0,0,0,x2,x3],[0,0,0,0,x8,-x9,0,x5,-x6],[2*x1,0,0,2*x4,0,0,0,0,0],[0,2*x2,0,0,2*x5,0,0,0,0],[0,0,2*x3,0,0,2*x6,0,0,0]))
J_i = lin.inv(J)
J_i = -1*J_i

i = True

while i:
    if all(np.round_(delta_x, decimals=7)) == 0:
        i = False
        
    delta_x = np.dot(J_i,f)
    
    guess += delta_x
    x1 = guess[0]
    x2 = guess[1]
    x3 = guess[2]
    x4 = guess[3]
    x5 = guess[4]
    x6 = guess[5]
    x7 = guess[6]
    x8 = guess[7]
    x9 = guess[8]
    
    f = np.array([3*x4 + 4*x5 + 4*x6 - 8,3*x1 + 4*x2 - 4*x3,x7*x1 - x8*x2 - 10,x7*x4 - x8*x5,x8*x2 + x9*x3 - 20,x8*x5 - x9*x6,x1**2 + x4**2 - 1, x2**2 + x5**2 - 1,x3**2 + x6**2 - 1])
    f = np.reshape(f,(9,1))
    J = np.array(([0,0,0,3,4,4,0,0,0],[3,4,-4,0,0,0,0,0,0],[x7,-x8,0,0,0,0,x1,-x2,0],[0,0,0,x7,-x8,0,x4,-x5,0],[0,x8,x9,0,0,0,0,x2,x3],[0,0,0,0,x8,-x9,0,x5,-x6],[2*x1,0,0,2*x4,0,0,0,0,0],[0,2*x2,0,0,2*x5,0,0,0,0],[0,0,2*x3,0,0,2*x6,0,0,0]))
    J_i = lin.inv(J)
    J_i = -1*J_i






theta1 = math.asin(guess[0])*(180/math.pi)
theta2 = math.asin(guess[1])*(180/math.pi)
theta3 = math.asin(guess[2])*(180/math.pi)

theta1c = math.acos(guess[3])*(180/math.pi)
theta2c = math.acos(guess[4])*(180/math.pi)
theta3c = math.acos(guess[5])*(180/math.pi)

