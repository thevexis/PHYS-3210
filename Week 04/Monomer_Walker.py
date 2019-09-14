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
y = 0
k = True
i = True
current_position = [[x,y]]
fig = plt.figure()
ax = fig.add_subplot(111)
spot = current_position[0]


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
        k = False
    else:
        current_position.append(new_position)
        spot = new_position
        i = True 
    
    
    ax.plot(current_position, "-")


plt.show()
    