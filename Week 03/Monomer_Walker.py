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


x = [0]
y = [0]
k = True

fig = plt.figure()
ax = fig.add_subplot(111)


while k:
    
    m = rand.randint(0,2)
    prev_position = [x,y]
    
    
    if prev_position[m] == [x]:
        x.append(x[-1] + (rand.randint(-1,2))
        new_position = [x,y]
    else:
        y.append(y[-1] + rand.randint(-1,2))
        new_position = [x,y]
        
    
    if new_position in prev_position:
        k = False
    else:
        prev_position = new_position
    
    
    ax.plot(prev_position, "-")


plt.show()
    