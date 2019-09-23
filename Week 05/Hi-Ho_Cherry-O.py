# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 17:34:07 2019

@author: thevexis

Exam 1
Hi-Ho Cherry-O


"""


import math as math
import numpy as np
import numpy.random as rand

Tree = 10
Basket = 0
rounds = 0

while Basket < 10:
    n = rand.randint(1,8)
    if n == 1:
        Basket += 1
        Tree -= 1
    elif n == 2:
        Basket += 2
        Tree -= 2
    elif n == 3:
        Basket += 3
        Tree -= 3
    elif n == 4:
        Basket += 4
        Tree -= 4
    elif n == 5 or n == 6:
        #Dog and Bird
        if Basket == 1:
            Basket -= 1
            Tree += 1
        elif Basket == 0:
            Basket = 0
            Tree = 10
        Basket -= 2
        Tree += 2
    elif n == 7:
        #Spill
        Tree += Basket
        Basket = 0
    rounds += 1
    
Basket = Basket - Basket%10
    
    
    
    
    
    
    
    
    
