# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 14:57:02 2019

@author: thevexis

Exam_03
van der Pol’s Equation & the Electric Field of a Laser

"""

import numpy as np
import matplotlib.pyplot as plt


def Laser(E,derE):
    
    w_0 = 1 # mode's natural frequency
    tau = 5 #loses
    g = 3 #gain from atomic emission
    g1 = 0.1 #saturation of gain
    start = 0 #time at zero
    stop = 180 #seconds have passed
    dt = 0.001 #interval of time (also h in euler and rk methods)
    t_array = np.arange(start,stop,dt)
    
    Electric_field = []
    Derivative_E = []
    
    
    """
    
    
    For solving the Van Der Pol's Equation I used an Euler method. 
    The equation d^2E/dt^2 = -(w_0**2)*E - (1/tau)*dE/dt + (g-(g1*(E**2)))*dE/dt
    was rewritten as Y_2 = -(w_0**2)*Y_0 - (1/tau)*Y_1 + (g-g1*(Y_0**2))*Y_1 where Y_1 is the first
    derivative and Y_2 is the second derivative. I choose the Euler method because while 
    the RK4 has less error it is more complicated and having a small step (dt) using the Euler method 
    would most certainly be accurate enough for this second order linear differential equation. I say 
    it would be accurate enough due to the simplicity of the equation and we are not solving for values
    with extensive significant figures.
    
    
    """
    
    Y_2 = -(w_0**2)*E - (1/tau)*derE + (g-(g1*(E**2)))*derE #initial conditions
    Y_1 = dt * Y_2
    Y_0 = dt * Y_1
    
    
    
    for t in t_array:
        
        Y_2 = -(w_0**2)*Y_0 - (1/tau)*Y_1 + (g-g1*(Y_0**2))*Y_1 
        Y_1 = dt * Y_2 + Y_1
        Y_0 = dt * Y_1 + Y_0
        
        Electric_field.append(Y_0)
        Derivative_E.append(Y_1)
        
    return Electric_field, Derivative_E, t_array

Electric_field, Derivative_E, time = Laser(1,0.1)

plt.plot(time, Electric_field)
plt.show()


plt.plot(Electric_field,Derivative_E)
plt.show()


"""

*note* w_0 = 1 in all of these figures

c.

At first when solving this when g1 = 0 I was getting overflow errors until adjusting the tau and g parameters. 
Figure 1 shows when g = 1/tau. In this case the phase space (orange) is still a closed loop though very thin,
meaning small changes in E have large changes in the derivative of E. Figure 2 shows when g > 1/tau with 
g = 1.3 and tau = 1. In this figure the Electric field over time increases very quickly and looks like a straight line 
because the time only goes to 180 seconds but the graph axes are now times 10**8. The phase space in red never creates a closed loop which might 
lead you to think that it is not harmonic, though given more time it could still make a loop. Figure 3 is similar to 
figure 2 though g = 2. Figure 4 shows this increase in the electric field with g = 1.15 and tau = 1 

d.

Figure 5 shows when g1 > 0.0  (g1 = 0.01,tau = 1, g = 1.15) the eletric field increases until it levels out and becomes harmonic
and at this point we can see the phase space does start to create a closed loop which does supports the idea that it becomes harmonic.

e.

Figure 6 is more inline with a typical van der Pol's osicillator graph (tau = 5, g = 3, g1 = 0.1)
The Van Der Pol's Equation is a second order linear differential equation that is a non-conservative oscillator. Now a relaxation oscillator 
in electronics is a nonlinear oscillator cicuit that produces a nonsinusoidal anharmonic ouput signal. 
We can see that under the given parameters this system is not random as it creates a closed symmetric loop 
which means that it is harmonic of some degree in this case anharmonic. The harmonic oscillator leads to symmetric ellipses however
in our case it is not an ellipse but a symmetric loop from the differential equation, again anharmonic. The closed orbits indicate periodic behavior. 
The size of the loop is determined by the amount of energy in the system. 

The orbits of anharmonic oscillations will still be ellipse like,
but with angular or curved corners that become more noticeable with increasing nonlinearity 
just as we see in the phase space of the the laser.
Closed trajectories describe periodic oscillations meaning the same E,E_dot occur again and again, 
with a clockwise motion arising from some restoring force.
There are a number of ways  to decide if a system is chaotic instead of just complex. 
Using phase space to find geometric scructures as we see in ours is one of them,
and determination of the Lyupanov coefficient (which has to do with the speration of the lines in phase space is another.
Both show an underlying simplicity within the complexity that we initially see.


Reading from the book we see: (I could not explain this very well while getting the full idea that was not basically what the text says)
'When a chaotic pendulum is driven by a not-too-large driving torque, 
it is possible to pick the magnitude for this torque such that after the initial transients die off,
the average energy put into the system during one period exactly balances the average energy 
dissipated by friction during that period
This leads to limit cycles that appear as closed ellipse-like figures. 
Yet unstable solutions may make sporadic jumps between limit cycles.'

We could see a limit cycle in the Van der Pol's equation. We could get closed ellipse-like figures
though if we made the g1 (saturation of the gain) zero and g greater we started to see the electric field 
increasing continually meaning that the average energy being inputed was greater than that being taken
away from the system in each period.

"""











