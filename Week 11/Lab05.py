# -*- coding: utf-8 -*-
"""
Anharmonic Oscillations with an RK2 Method

Created on Wed Oct 23 10:18:14 2019

@author: gafeiden
"""
import numpy as np
import matplotlib.pyplot as plt

def frictionForce(m, v, mu_s = 0.0, mu_k = 0.0, turning=False):
    """ Calculate force from static and kinetic friction """
    # local acceleration due to gravity
    g = 9.81   # [m/s**2]
    
    # force from kinetic friction [N]
    if turning:
        f_static  = -mu_s * m * g
        f_kinetic = 0.0 
    else:
        f_static  = 0.0 
        f_kinetic = -mu_k * m * g * v / abs(v + 1.0e-16)
    
    return np.array([f_static, f_kinetic])

def springForce(k, x, p):
    """ Calculate the spring force """
    return -k*x**(p - 1)

def rk2Solve(m, x0, v0, k=1.0, p=2, dt=1.0e-2):
    """ Solve the anharmonic oscillator using RK2 """
    v_list = [v0]
    x_list = [x0]
    
    t = 0.0  # initial time [s]
    t_list = [t]
    turning = True
    for i in range(int(20/dt)):
        t += dt
        
        F_friction = frictionForce(m, v0, mu_s = 0.1, mu_k = 0.1, turning=turning)
        F_spring   = springForce(k, x0, p)
        
        # determine velocity at the mid-point
        if turning:
            # check whether spring force will overcome static friction
            stuck = (abs(F_spring) <= abs(F_friction[0]))
            if stuck:
                v12 = 0.0
            else:
                v12 = v0 + dt*F_spring/2.0/m + dt*F_friction[0]/2.0/m
        else:
            stuck = False
            v12 = v0 + dt*F_spring/2.0/m + dt*F_friction[1]/2.0/m
        
        # position at the mid-point
        x12 = x0 + dt*v0/2.0
        
        # calculate whether the mass is at a turning point
        turning = (v0/(v12 + 1.0e-16) < 0.0)
        
        # compute forces on the mass
        F_friction = frictionForce(m, v12, mu_s = 0.1, mu_k = 0.1, turning=turning)
        F_spring   = springForce(k, x12, p)
        
        if turning:
            stuck = (abs(F_spring) <= abs(F_friction[0]))
            if stuck:
                v0 = 0.0
                #break
            else:
                v0 += dt*F_spring + dt*F_friction[0]/m
        else:
            stuck = False
            v0 += dt*F_spring + dt*F_friction[1]/m
        x0 += dt*v12
    
        v_list.append(v0)
        x_list.append(x0)
        t_list.append(t)
        
    t_list = np.array(t_list)
    x_list = np.array(x_list)
    v_list = np.array(v_list)
    
    solution = np.column_stack((t_list, x_list))
    solution = np.column_stack((solution, v_list))
    
    return solution

def eulerSolve(m, x0, v0, k=1.0, p=2, dt=1.0e-2):
    """ Solve the anharmonic oscillator using Euler's method """
    v_list = [v0]
    x_list = [x0]
    
    t = 0.0  # initial time [s]
    t_list = [t]
    for i in range(int(20/dt)):
        t  += dt
        v0 += dt/m * springForce(k, x0, p)
        x0 += v0*dt
        
        v_list.append(v0)
        x_list.append(x0)
        t_list.append(t)
        
    t_list = np.array(t_list)
    x_list = np.array(x_list)
    v_list = np.array(v_list)
    
    solution = np.column_stack((t_list, x_list))
    solution = np.column_stack((solution, v_list))
    
    return solution

# initial conditions of mass
m  = 5.0  # object's mass [kg]
v0 = 0.0  # object's initial x velocity [m/s]
x0 = 2.0  # object's initial position [m]

# spring constant
k = 10.0   # 

dt = 1.0e-3  # time step [s]

p02_rk = rk2Solve(m, x0, v0, k=k, p=2,  dt=dt)
p03_rk = rk2Solve(m, x0, v0, k=5.0, p=2,  dt=dt)
#p06_rk = rk2Solve(m, x0, v0, k=k, p=6,  dt=dt)
#p10_rk = rk2Solve(m, x0, v0, k=k, p=10, dt=dt)

p02_em = eulerSolve(m, x0, v0, k=k, p=2,  dt=dt)
p06_em = eulerSolve(m, x0, v0, k=k, p=6,  dt=dt)
#p10_em = eulerSolve(m, x0, v0, k=k, p=10, dt=dt)


fig, ax = plt.subplots(1, 2)
# Position vs Time, RK2
ax[0].plot(p02_rk[:,1], p02_rk[:,0], '-', lw=2)
ax[0].plot(p03_rk[:,1], p03_rk[:,0], '-', lw=2)
#ax[0].plot(p06_rk[:,1], p06_rk[:,0], '-', lw=2)
#ax[0].plot(p10_rk[:,1], p10_rk[:,0], '-', lw=2)
ax[0].set_title("RK2 :: Position vs Time")
ax[0].set_xlabel("Position [m]")
ax[0].set_ylabel("Time [s]") 

# Velocity vs Time, RK2
ax[1].plot(p02_rk[:,2], p02_rk[:,0], '-', lw=2)
ax[1].plot(p03_rk[:,2], p03_rk[:,0], '-', lw=2)
#ax[1].plot(p06_rk[:,2], p06_rk[:,0], '-', lw=2)
#ax[1].plot(p10_rk[:,2], p10_rk[:,0], '-', lw=2)
ax[1].set_title("RK2 :: Velocity vs Time")
ax[1].set_xlabel("Velocity [m/s]")
ax[1].set_ylabel("Time [s]") 

fig.tight_layout()
plt.show()


fig, ax = plt.subplots(1, 2)

# Position vs Time, Euler
ax[0].plot(p02_em[:,1], p02_em[:,0], '-', lw=2)
ax[0].plot(p06_em[:,1], p06_em[:,0], '-', lw=2)
#ax[0].plot(p10_em[:,1], p10_em[:,0], '-', lw=2)
ax[0].set_title("Euler :: Position vs Time")
ax[0].set_xlabel("Position [m]")
ax[0].set_ylabel("Time [s]") 

# Velocity vs Time, Euler
ax[1].plot(p02_em[:,2], p02_em[:,0], '-', lw=2)
ax[1].plot(p06_em[:,2], p06_em[:,0], '-', lw=2)
#ax[1].plot(p10_em[:,2], p10_em[:,0], '-', lw=2)
ax[1].set_title("Euler :: Velocity vs Time")
ax[1].set_xlabel("Velocity [m/s]")
ax[1].set_ylabel("Time [s]") 

fig.tight_layout()

plt.show()
