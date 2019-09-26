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




x_array =  np.arange(0,1,0.001)

function_x1 = x_array**2
function_x2 = x_array**2
function_x3 = x_array**2
function_x4 = x_array**2
function_x5 = x_array**2
function_x6 = x_array**2
function_x7 = x_array**2
function_x8 = x_array**2
function_x9 = x_array**2
function_x10 = x_array**2

big_function = ([function_x1, function_x2, function_x3, function_x4, function_x5, function_x6, function_x7, function_x8, function_x9, function_x10])

summation = 0
top = len(function_x)

for i in range(100):
    n = rand.randint(0,top)
    l = rand.randint(1,11)
    






