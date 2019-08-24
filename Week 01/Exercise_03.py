# -*- coding: utf-8 -*-
"""
Exercise 03: Chapter 03, Kinder & Nelson

A common way to determine the value of a function is to sum over a series. 
For example, the Maclaurin series for sin(x) is

    sin(x) = x - x**3/3! + x**5/5! - x**7/7! + ...

Perform a series expansion to derive the equation above. Next, write down 
a general expression for the sum of the series that is valid between n = 0 
and n = N, where N ≥ 0. This will serve as your algorithm for summing 
the series.

One problem with the algorithm is that we do not know which value 
of N is suitable when calcualting the series. Instead of guessing, have 
your code proceed with the summation until the Nth term contributes a 
negligible amount to the final summation, say 1 part in 10**8.

Before writing any lines of code, discuss an approach with your neighbor 
and write out on paper how your code should proceed. Code up your approach 
in Spyder once you're done. 

Here are your tasks:

   1. Perform a Maclaurin series expansion of the function sin(x) to 
      derive the equation in the README. 
   2. Derive a generalized, finite summation form for the series based 
      on your Maclaurin series expansion.
   3. Discuss with your neighbor about how to approach coding the problem
      and write out on paper how you code should proceed. 
   4. Code your approach in Spyder once you are finished.
   5. Show that, for small values of x, the series converges.
   6. Which value for N was required to reach the desired precision and
      obtain convergence?
   7. Compare your results to the value determined using NumPy's sine 
      function.
   8. Steadily increase x and write down the relative error between your
      calculated value for sin(x) and the NumPy function's value. 
   9. What do you notice about the relative error?
  10. Will there be a time when the series does not converge? Make a plot
      of the relative error vs x to support your answer.

Created on Tue Aug 20 11:02:00 2019

@author: gafeiden
"""
import math as math

x_input = input("Enter a value x to recieve sin(x): ", )
x = float(x_input)

finite_sum_N = input("Enter a number, where larger numbers increase accuracy: ", )
N = int(finite_sum_N)

if N > 10000:
    print("Too many approximations!")
    finite_sum_N = input("Enter a number, where larger numbers increase accuracy: ", )



sine_actual = math.sin(x)

def my_factorial(k):
    if k == 0:
        return 1
    else:
        return k * my_factorial(k-1)

for n in range(0, N):
    
    k = (2*n)+1
    sine_x = 0
    function = ((-1)**n)*(x**((2*n)+1))/(my_factorial(k))
    sine_x += function
    
    if  sine_actual < sine_x:
        print("It takes ", n, "approximations to converge.")
        break
    
sine_x_f = "{0:.6f}".format(sine_x)  
  
print("Approximation of sine fuction is ", sine_x_f)
print("Actual sine fuction gives: ", sine_actual)
error = (sine_actual - sine_x)/(sine_actual)*100
print("The error of approximation is ", error,"%")
    
    
    
    
    
    