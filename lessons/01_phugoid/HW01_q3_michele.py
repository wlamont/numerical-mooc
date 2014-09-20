# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 21:03:48 2014

@author: wlamont
"""

# LIBRARY IMPORT
from math import sin, cos, log, ceil, pi
import numpy
import matplotlib.pyplot as plt
#%matplotlib inline
from matplotlib import rcParams
rcParams['font.family'] = 'serif'
rcParams['font.size'] = 16

mp0 = 100.   #'initial fuel mass [kg]"
rate = 20.   #'decreasing constant burrning rate'
ms = 50.     #'rocket shell weight [kg]
g = 9.81     #'gravity [m/s^2]
r = 0.5      #' rocket radius'
ve = 325.     #'fume exhausted
Cd = 0.15
rho = 1.091

#TIME DISCRETIZATION

dt = 0.1
T = 100.
N = int(T/dt) + 1 #number of steps
t = numpy.linspace(0.0,T,N) #array of time grid

#def burnRate(A,rate,t):
#    '''calculate the burn rate for rocket, rate is constant
#        rate = rate of decreasing
#        t: timegrid'''
#      
mp = numpy.zeros_like(t)
   
mp[0]=mp0
for i in range(0,N):
    if mp[i]<0:
        mp[i]=0
        break
    else:
        mp[i+1]=mp[i]-rate*dt
          

    
#CALCULATION OF DERIVED PARAMETERS

fArea = pi*r**2
mTot = numpy.zeros_like(t)   #(ms+mp)
rate_mp = numpy.zeros_like(t) #array for thrust
C1 = numpy.zeros_like(t) #constant for burnrate
C2 = numpy.zeros_like(t) #constant for kinetic
j=0
for i in range(0,N):
    if mp[i]!=0:
        rate_mp[i]=rate
    mTot[i]=ms+mp[i]  
    C1[i] = rate_mp[i]/mTot[i]
    C2[i] = fArea*Cd*rho/mTot[i]
    
v = numpy.zeros_like(t)
h = numpy.zeros_like(t)

for i in range (0,N):
    if h[i]<0:
        break
    else:
        v[i+1]=v[i]+dt*(-g+C1[i]*ve-0.5*C2[i]*v[i]**2)
        h[i+1]=h[i]+dt*v[i]
        
#RESULTS
maxV=numpy.amax(v)
minV=numpy.amin(v)
maxH=numpy.amax(h)

print maxV, minV, maxH

for i,j in enumerate(v):
    if j==maxV:
        print t[i]
        print h[i]
        
for i,j in enumerate(h):
    if j==maxH:
        print t[i]
        
#PLOTTING
plt.figure(figsize=(6,6))
plt.grid(True)
plt.tick_params(axis='both', labelsize=14) #increase font size for ticks
plt.xlabel(r'x', fontsize=18)
plt.ylabel(r'v', fontsize=18)
plt.plot(t,v)
plt.plot(t,h)
plt.legend(['velocity','height']);