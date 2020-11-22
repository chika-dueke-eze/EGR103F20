"""
[chapra_6_036.py]
[Chika Dueke-Eze]
[11-17-2020]
Based on: pundit code
Written by: Michael R. Gustafson II

I understand and have adhered to all the tenets of the Duke Community Standard
in creating this code.
Signed: [chika]
"""

#%% initialize workspace
import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt

k = 1.4
R = 287
Ta = 277
theta = 4 * np.pi/180
v = 625
c = np.sqrt(k*Ta*R)
M = v/c
p = 110

B = np.linspace(2*np.pi/180,88*np.pi/180,100)
def_ang = ((2 * (M**2 * np.sin(B)**2 - 1)) / (np.tan(B) * M**2 * (1.4 + np.cos(2 * B) + 2))) - np.tan(theta)

#%% initialize & plot graph
fig, ax = plt.subplots(num=1, clear=True)
fig.set_size_inches(6, 4, forward=True)
 
#plot graphs (y as a function of x)
ax.plot(B, def_ang)


# Label and title the graph
ax.set(
    xlabel = "shock angle",
    ylabel = "tan(deflection angle)",
    title = "tan(deflection angle) vs shock angle"
) 

ax.grid(True)
ax.legend(loc="best")

fig.tight_layout() #tighten layout

#save
fig.savefig('chapra_6_036_plot.png') 

#%%find roots
r1 = opt.brentq(lambda B: ((2 * (M**2 * np.sin(B)**2 - 1)) / (np.tan(B) * M**2 * (1.4 + np.cos(2 * B) + 2))) - np.tan(theta), 0, 1)
print(r1)

#%%solve for Pa
B = r1
Pa = p * (((2*k)/(k+1)) * ((M*np.sin(B))**2) - ((k-1)/(k+1)))
print(Pa)
