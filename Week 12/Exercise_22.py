# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 09:58:19 2019

@author: thevexis

Exercise_22
Shooting for an Eigenvalue Solution
"""

import matplotlib.pyplot as plt
import math as math
import numpy as np



E = 1 #MeV
k = 0.0483 * E #MeV^-1 fm^-2


def Psi_R(x):
    return np.exp(-k*x)
def d2Psi_R(x):
    return (k**2)*np.exp(-k*x)
def Psi_L(x):
    return np.exp(k*x)

Xmax = 1
Xmatch = 0
total = 0

for step in range(Xmax,Xmatch):
    total += Psi_R(step)
    


