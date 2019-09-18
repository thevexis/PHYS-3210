# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 10:08:54 2019

@author: thevexis

Exercise_08
Derivatives:
The derivative refers to the slope of a line at any given point on a function and 
can sometimes be expressed as another function. If we have f(x) = x^2 then we can find 
the slope of the line at any two points, say x = 0 and x = 1. Using our slope formula rise 
over run we see that the slope is 1. We can do this between any two points but if we want to find the slope
at a specific one point we will need to make the distance between the two points arbitralily small so we can have our 
point x and another point x + h where h is really small and we can say approaches zero. 
Then we can just use our slope formula and the 'run' will be x - x + h or just h, and the rise
will be f(x+h) - f(x). Now we put all this into one equation with a limit as h approaches zero and we get 
lim h --> 0 ((f(x+h) - f(x))/h). And that is our derivative.   
    
"""

import matplotlib.pyplot as plt
import math as math
import numpy as np

start = -2*math.pi
stop = 2*math.pi + 0.000000001
h = 0.0001
x_array = np.arange(start, stop, h)
sine_x_array = np.sin(x_array)

df = np.gradient(sine_x_array,h)


def derivative(f,h):
    i = 0
    df = []
    while i < len(f)-1:
        df.append((f[i+1] - f[i])/h)
        i += 1
    return df




function = derivative(sine_x_array,h)

x = x_array[:-1]

#print("This is Cosine:", function)

plt.plot(x, function, "r")
plt.show()

print("This is Sine:", sine_x_array)
plt.plot(x_array, sine_x_array)
plt.show()


plt.plot(x, function, "r")
plt.plot(x_array, sine_x_array )
plt.show()


#Graph of numpys gradient and mine are so close to the same you do not see a difference on the graph
plt.plot(x, function, "r")
plt.plot(x_array, df )
plt.show()

#second derivative with np gradient function
df2 = np.gradient(df,h)
plt.plot(x_array, df2, "g")
plt.show()

x = x[:-1]
#second derivative
function2 = derivative(function,h)
plt.plot(x, function2, "y")
plt.show()