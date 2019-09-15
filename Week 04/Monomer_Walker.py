# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 09:02:56 2019

@author: theve
"""

"""
Lab 03 ----- Monomers
Note: that in rand.randint() (0,1) sometimes does 0 and 1 but sometimes does just 0
so you need (0,2) to have both 0 and 1. Don't know why

"""


import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt


x = 0
y = 1
k = True
i = True
current_position = [[x,y]]
fig = plt.figure()
ax = fig.add_subplot(111)
spot = current_position[0]
m = True 


while k:
    
    m = rand.randint(0,2)
    direction = rand.randint(-1,2)
    
    
    while i:
        if spot[m] == x:
            new_x = x + direction 
            new_position = [new_x,y]    
        else:
            new_y = y + direction 
            new_position = [x,new_y]
            
        if new_position != spot:
            i = False
        else:
            direction = rand.randint(-1,2)
    
    
    if new_position in current_position:
        W = new_position[0] + 1
        E = new_position[0] - 1
        N = new_position[1] + 1
        S = new_position[1] - 1
        West = [W,new_y]
        East = [E,new_y]
        North = [new_x,N]
        South = [new_x,S]
        if West in current_position and East in current_position and North in current_position and South in current_position:
            k = False
        else:
            while m:
                v = rand.randint(0,4)
                if v == 0:
                    new_position = West
                    if new_position not in current_position:
                        m = False
                elif v == 1:
                    new_position = East
                    if new_position not in current_position:
                        m = False
                elif v == 2:
                    new_position = North
                    if new_position not in current_position:
                        m = False
                elif v == 3:
                    new_position = South
                    if new_position not in current_position:
                        m = False
            
    else:
        current_position.append(new_position)
        spot = new_position
        i = True 
        x = new_position[0]
        y = new_position[1]
    
    
    ax.plot(current_position, "-")


plt.show()
    