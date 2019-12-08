# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 10:02:18 2019

@author: thevexis
"""

import math as math
import matplotlib.pyplot as plt
import numpy as np
 


N = 1000

summ = 0

for n in range(1,N+1):
    summ += (1/n)
    
print(summ)

summ2 = 0

for n in range(N,0,-1):
    summ2 += (1/n)
    
    
print(summ2)

error = ((summ2 - summ) /(summ2)) * 100

print("Error between round up and round down is ", error,"%")

fig = plt.figure()
ax = fig.add_subplot(111)

summ = 0
summ2 = 0

for n in range(1,N+1):
    summ += (1/n)
    for k in range(N,0,-1):
        summ2 += (1/k)
    y = ((summ - summ2)/(abs(summ) + abs(summ2)))
    p = ax.plot(n, y, 'o', c='r')

ax.set_xlabel('N')
ax.set_ylabel('Thingy')
ax.set_title('Round Up vs Round Down')
fig.show()



