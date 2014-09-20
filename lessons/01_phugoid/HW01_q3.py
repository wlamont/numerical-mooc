# -*- coding: utf-8 -*-
"""
Created on Sun Sep 14 10:42:49 2014

@author: wlamont

Rocket Flight assignment
"""

import numpy as np
import matplotlib.pyplot as plt


#inputs

ms  = 50.0 # weight of the rocket shell (kg)
g   = 9.81 #gravitational constant (m/s^2)
rho = 1.091 #air density (kg/m^3)
A   = np.pi * (0.5) ** 2.0 #cross section of the rocket (m^2)
ve  = 325.0 #exhaust speed (m/s)
Cd  = 0.15  #drag coefficient
mp  = np.asarray([100.0]) #initial weight of rocket propellant at t = 0 


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
    
    omega = (-(ms + mp[-1]) * g + mp_dot[-1] * ve - 0.5 * rho * A * Cd * (v[-1] * abs(v[-1]))) / (ms + mp[-1])
    
#    omega2 = -g + mp_dot[-1] * ve / (ms + mp[-1]) - 0.5 * rho * A * Cd * (v[-1] * abs(v[-1])) / (ms + mp[-1])
    
    v = np.append(v, v[-1] + dt * omega)
    
    if t[-1] < 4.9999:
        mp = np.append(mp, mp[0] - t[-1] * 20.0) #mass of propellant remaining
        mp_dot = np.append(mp_dot, 20.0) #burn rate
    else:
        mp = np.append(mp, 0)
        mp_dot = np.append(mp_dot, 0.0) #no more propellant

#h[-1] = 0 
#dt2     = (h[-1] - h[-2]) / v[-2]
#t[-1]   = t[-2] + dt2
#v[-1]   = v[-2] + dt2 * omega
    
    
    
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

plt.figure(figsize=(6,6))
plt.grid(True)
plt.xlabel('t (s)', fontsize=18)
plt.ylabel('mp dot (kg/s)', fontsize=18)
plt.plot(t, v, 'b-');   
plt.plot(t, h, 'g-');  

print 'Done!'
    
    
    
        
    
    
    

