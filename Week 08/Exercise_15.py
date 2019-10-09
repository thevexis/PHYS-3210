# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 10:05:05 2019

@author: thevexis
Exercise_15
Finding Bound State Energies
"""


import matplotlib.pyplot as plt
import math as math
import numpy as np
import numpy.random as rand
import numpy.linalg as lin 
import scipy.optimize as opt


x_array = np.arange(-20,10,0.01)

c = ((10-x_array)**(1/2))
y = c * np.tan(c) - ((x_array)**(1/2))


def f(x):
    return ((10-x)**(1/2)) * np.tan(((10-x)**(1/2))) - ((x)**(1/2))
    
bisect1 = opt.bisect(f,8,9)

plt.plot(x_array, y)
plt.ylim(-20,20)


zero_point = opt.newton(f,8)
zero_point2 = opt.newton(f,0)

accuracy = f(zero_point)
accuracy2 = f(zero_point2)

"""
We can see by the values of our functions at the zero points that they are very close to zero
so the newton optimizing method is quite accurate to 10^-14 10^-16 decimal places.

The even function can simply be rewritten by adding the square root of E_b 
dividing by tan((10-E_b)**0.5) and then subtracting ((10-E_b)**0.5) so that we get:
"""


y2 = -1*((10-x_array)**(1/2)) + (np.tan(((10-x_array)**(1/2)))*-1) * ((x_array)**(1/2))

plt.plot(x_array, y2,'r')
plt.ylim(-20,20)
plt.show()
print("Comparison of two forms of the even solution"\n)

def g(x):
    return -1*((10-x)**(1/2)) + (np.tan(((10-x)**(1/2)))*-1) * ((x)**(1/2))


zero_point3 = opt.newton(g,4)
zero_point4 = opt.newton(g,10)

accuracy3 = g(zero_point3)
accuracy4 = g(zero_point4)

"""
We find new zero points with this equation 

"""



y3 = -1*((20-x_array)**(1/2)) + (np.tan(((20-x_array)**(1/2)))*-1) * ((x_array)**(1/2))

plt.plot(x_array, y3,'g')
plt.ylim(-50,50)


y3 = -1*((30-x_array)**(1/2)) + (np.tan(((30-x_array)**(1/2)))*-1) * ((x_array)**(1/2))

plt.plot(x_array, y3,'y')
plt.ylim(-50,50)
plt.show()

print("Comparison of 20 and 30 Binding Energy")


"""
Binding Potential of 30 looks about the same as with 10 but 20 gives you a completely
different graph.

"""





