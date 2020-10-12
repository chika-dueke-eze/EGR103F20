SCRIPT FOR SOLVING PROBLEM 02.013

#%% 
import numpy as np


f = np.array([16,20,10,11,15])
x = np.array([0.013,0.020,0.009,0.010,0.012])
k = f/x
u = 0.5 * k * x**2

print(max(u))
