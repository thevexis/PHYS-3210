# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 10:03:39 2019

@author: thevexis

Exercise_14
Linear Algebra Routines
"""

import matplotlib.pyplot as plt
import math as math
import numpy as np
import numpy.random as rand
import numpy.linalg as lin 


A = np.array(([4,-2,1],[3,6,-4],[2,1,8]))
B = lin.inv(A)

b1 = np.array(([12],[-25],[32]))
b2 = np.array(([4],[-10],[22]))
b3 = np.array(([12],[-30],[40]))


x1 = lin.solve(A,b1)
x2 = lin.solve(A,b2)
x3 = lin.solve(A,b3)

M = np.array(([2,3],[-3,2]))
eigen = lin.eigvals(M)

N = np.array(([-2,2,-3],[2,1,-6],[-1,-2,0]))
e = lin.eigvals(N)

y1 = np.array(([-1],[-2],[1])) * (1/math.sqrt(6))







