# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 17:34:07 2019

@author: thevexis

Exam 1
Hi-Ho Cherry-O


"""

import matplotlib.pyplot as plt
import math as math
import numpy as np
import numpy.random as rand


#Never Game with the same size for every section on the spinner

average = []
print("Same spacing")
for i in range(100):
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
    average.append(rounds)
    
plt.hist(average)
plt.xlabel("Number of Rounds")
plt.ylabel("Frequency")
plt.savefig("Even_Spaced.png")
plt.show()


#Old Game with double size on the spinner for picking cherrys

old_average = []
print("Uneven spacing")
for i in range(100):
    Old_Tree = 10
    Old_Basket = 0
    Old_rounds = 0
    while Old_Basket < 10:
        n = rand.randint(1,12)
        if n == 1 or n == 2:
            Old_Basket += 1
            Old_Tree -= 1
        elif n == 3 or n == 4:
            Old_Basket += 2
            Old_Tree -= 2
        elif n == 5 or n == 6:
            Old_Basket += 3
            Old_Tree -= 3
        elif n == 7 or n == 8:
            Old_Basket += 4
            Old_Tree -= 4
        elif n == 9 or n == 10:
            #Dog and Bird
            if Basket == 1:
                Old_Basket -= 1
                Old_Tree += 1
            elif Basket == 0:
                Old_Basket = 0
                Old_Tree = 10
            Old_Basket -= 2
            Old_Tree += 2
        elif n == 11:
            #Spill
            Old_Tree += Old_Basket
            Old_Basket = 0
        Old_rounds += 1
    old_average.append(Old_rounds)
    
 
plt.hist(old_average)
plt.xlabel("Number of Round")
plt.ylabel("Frequency")
plt.savefig("Uneven_Spaced.png")
plt.show()

    

    
"""




"""
    
