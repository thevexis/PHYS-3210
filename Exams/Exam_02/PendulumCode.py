# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 21:44:05 2019

@author: thevexis
Exam_02
Pendulum
"""

import numpy as np
import matplotlib.pyplot as plt


"""
Using an Euler Method due to its simple and more concise method. The Euler method is accurate than a
RK2 or higher but is less computationally expensive and is quicker to code. I am also not too concerned
with having a great deal of accuracy as I do not need an extensive amount of significant figures for
this solution. The accuracy accquired by an Euler method with my step (dt) being 0.001 is acceptable 
for this problem.

"""

def Pendulum(Initial_angle,length):
    
    Initial_angle = (Initial_angle *np.pi)/180
    g = 9.8 #m/s^2 acceleration due to gravity
    start = 0 #time at zero
    stop = 60 #seconds have passed
    dt = 0.001 #interval of time (also h in euler and rk methods)
    t_array = np.arange(start,stop,dt)

    x = []
    y = []
    
    vx = []  #velocities of cartesian space
    vy = []
    
    theta = [] #used for the phase space
    theta_dot = []
    
    
    y_2 = (-g/length)*np.sin(Initial_angle) #initial conditions
    y_1 = dt*y_2
    y_0 = dt*y_1
    
    Theoretical_Period = 2*np.pi*((length/g)**0.5)
    Period = []

    for t in t_array:
        
        y_2 = (-g/length)*np.sin(y_0)
        y_1 = dt * y_2 + y_1
        
        #derivative of the x position should be zero when pendulum is at its highest position
        #second derivative of the x position ensures coming from same direction i.e. full period
        if np.round_((np.sin((y_1*np.pi)/180)), decimals=8) == 0 and np.sin((y_2*np.pi)/180) > 0:
            #print(t) used for testing 
            Period.append(t)
        
        y_0 = dt * y_1 + y_0
        
        vx.append(length*np.sin((y_1*np.pi)/180))
        vy.append(length*np.cos((y_1*np.pi)/180))
        
        x.append(length*np.sin((y_0*np.pi)/180))
        y.append(length*-np.cos((y_0*np.pi)/180))
        
        theta.append(y_0)
        theta_dot.append(y_1)
    
    for l in range(1,len(Period)):
        if (Period[l] - Period[l-1]) > 1:
            Actual_Period = Period[l] - Period[l-1] 
    
    
    return x ,y , theta, theta_dot, t_array, Theoretical_Period, Actual_Period, vx, vy

x, y, theta, theta_dot, t_array, Theoretical_Period, Actual_Period, vx, vy = Pendulum(45,40) #length must be long enough for pendulum to start

plt.plot(x,y)
plt.title('Cartesian Space')
plt.show()

plt.plot(vx,vy,'black')
plt.title('Velocity Cartesian Space')
plt.show()

print('Actual Period:', Actual_Period)
print('Theoretical Period:',Theoretical_Period)


Period_Error = (Actual_Period - Theoretical_Period)/Theoretical_Period * 100
print("At this angel the error in the actual and theoretical period is:", Period_Error,"%")

plt.plot(theta_dot,theta,'r')
plt.title('Phase Space')
plt.show()

"""
multiple angels

The larger the initial angle the greater the period (slightly due to parameters)
"""
for k in range(30,70,5):
    x, y, theta, theta_dot, t_array, Theoretical_Period, Actual_Period, vx, vy = Pendulum(k,40) #length must be long enough for pendulum to start

    plt.plot(t_array,x)

    print('With Angle ',k)
    print('Actual Period:', Actual_Period)
    print('Theoretical Period:',Theoretical_Period)
    Period_Error = (Actual_Period - Theoretical_Period)/Theoretical_Period * 100
    print("At this angel the error in the actual and theoretical period is:", Period_Error,"%")
    



"""

The Cartesian Space plot and the Velocity Cartesian Space plot makes a parabola which is the exact path a 
pendelum normally follows from its starting angle to its maximum velocity
at the center of its path to the same absolute angle with opposite sign. Of course we would expect the
cartesian plane to look like what it does when you swing a pendulum
The Equation for the period of the pendulum theoretically does not depend on
theta, however this is due to the assumption made when creating the equation. 
The assumption being that the sin(theta) = theta which holds true for small 
angles and is therefore called the small angle assumption. For larger angle above 15 degrees 
this error between the period found with this equation and the actual period will star to increase
however due to a complication in finding the actual period (aka my method for finding it was crude and
has manny errors) this code shows the opposite affect. The phase space diagram which uses 
the variables of the angle and the change in the angle creates a circle. This is because theta and its 
derivative follow a sinusoidal motion over time and so if theta is similar to the cosine(t) then 
the derivative will follow as the sine(t) thus at theta approaches its maximum (highest angle or position)
then theta dot approaches zero and then as theta dot approaches its maximum (highest velocity) then
theta approaches zero. This continued will create a circle or an ellipse depending on if the maximum are
the same.

"""

"""
Friction Challenge
"""

def PendulumFriction(Initial_angle,length,mass):
    
    c = 1.0e-3 #friction coefficient
    Initial_angle = (Initial_angle *np.pi)/180
    g = 9.8 #m/s^2 acceleration due to gravity
    start = 0 #time at zero
    stop = 240 #seconds have passed
    dt = .001 #interval of time (also h in euler and rk methods)
    t_array = np.arange(start,stop,dt)

    x = []
    y = []
    
    theta = [] #used for the phase space
    theta_dot = []
    
    y_2 = (-g)*np.sin(Initial_angle) - (c/mass)*length*(0) #initial conditions
    y_1 = dt*y_2
    y_0 = dt*y_1
    
    Theoretical_Period = 2*np.pi*((length/g)**0.5)
    Period = []

    for t in t_array:
        
        y_2 = (-g/length)*np.sin(y_0) - (c/mass)*length*y_1
        y_1 = dt * y_2 + y_1
        y_0 = dt * y_1 + y_0
        
        
        
        x.append(length*np.sin((y_0*np.pi)/180))
        y.append(length*-np.cos((y_0*np.pi)/180))
        
        theta.append(y_0)
        theta_dot.append(y_1)

    
    
    return x ,y , theta, theta_dot, t_array

x, y, theta, theta_dot, t= PendulumFriction(45,400,10)

plt.plot(x,y,'y')
plt.title('Cartesian Space with Friction')
plt.show()

plt.plot(t,x,'g')
plt.title('Position as Function of Time X(t)')
plt.show()

"""

Due to friction in the form of air resistance the pendulum cannot return to its original height
and therefore its amplitude gets smaller each time and the position starts return to zero which is
at rest.

"""
