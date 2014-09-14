# -*- coding: utf-8 -*-
"""
Created on Sun Sep 14 10:42:49 2014

@author: wlamont

Rocket Flight assignment
"""

import numpy as np
import matplotlib.pyplot as plt


#inputs

ms  = 50 # weight of the rocket shell (kg)
g   = 9.81 #gravitational constant (m/s^2)
rho = 1.091 #air density (kg/m^3)
A   = np.pi * (0.5) ** 2 #cross section of the rocket (m^2)
ve  = 325 #exhaust speed (m/s)
Cd  = 0.15  #drag coefficient
mp  = np.asarray([100]) #initial weight of rocket propellant at t = 0 


dt  = 0.1 #time step (s)

#initialize arrays

h = np.asarray([0.0])
t = np.asarray([0.0])
v = np.asarray([0.0])
mp_dot = np.asarray([20.0])

while h[-1] >= 0.0:

#for i in range(0, 300):
    
    t = np.append(t, t[-1] + dt)
 
    h = np.append(h, h[-1] + dt * v[-1])
    
    omega = (-(ms + mp[-1]) * g + mp_dot[-1] * ve - 0.5 * rho * A * Cd * (v[-1]) ** 2.0) / (ms + mp[-1])
    
    v = np.append(v, v[-1] + dt * omega)
    
    if t[-1] < 4.99:
        mp = np.append(mp, mp[0] - t[-1] * 20) #mass of propellant remaining
        mp_dot = np.append(mp_dot, 20) #burn rate
    else:
        mp = np.append(mp, 0)
        mp_dot = np.append(mp_dot, 0.0) #no more propellant
    
    
    
#    print h[-1]
#    print h[-1], t[-1], v[-1]

plt.figure(figsize=(6,6))
plt.grid(True)
plt.xlabel('t (s)', fontsize=18)
plt.ylabel('h (m)', fontsize=18)
plt.plot(t, h, 'k-');

plt.figure(figsize=(6,6))
plt.grid(True)
plt.xlabel('t (s)', fontsize=18)
plt.ylabel('v (m/s)', fontsize=18)
plt.plot(t, v, 'k-');

plt.figure(figsize=(6,6))
plt.grid(True)
plt.xlabel('t (s)', fontsize=18)
plt.ylabel('mp (kg)', fontsize=18)
plt.plot(t, mp, 'k-');
 
plt.figure(figsize=(6,6))
plt.grid(True)
plt.xlabel('t (s)', fontsize=18)
plt.ylabel('mp dot (kg/s)', fontsize=18)
plt.plot(t, mp_dot, 'k-');   

print 'Done!'
    
    
    
        
    
    
    

