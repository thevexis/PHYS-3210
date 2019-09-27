# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 10:13:38 2019

@author: thevexis

Exercise_12
MC Method Higher Dimension Integrals

"""

import matplotlib.pyplot as plt
import math as math
import numpy as np
import numpy.random as rand

N=1000
summation = []
b = 1
a = 0

for i in range(N): 
    for l in range(10):
        x = rand.rand(10)*(b-a)
        f = sum(x)
        function = f**2
    summation.append(function)
    
summation = sum(summation)/N
    
print(summation)





