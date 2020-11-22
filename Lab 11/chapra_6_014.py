"""
[chapra_6_014.py]
[Chika Dueke-Eze]
[11-17-2020]
Based on: pundit code
Written by: Michael R. Gustafson II

I understand and have adhered to all the tenets of the Duke Community Standard
in creating this code.
Signed: [chika]
"""

import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt

#%% load values
x = np.linspace(0,0.05,10000)
K =  -0.05 + (x/(1-x)) * np.sqrt(6/(2+x))

#%% initialize graph
fig, ax = plt.subplots(num=1, clear=True)
fig.set_size_inches(6, 4, forward=True)
 
#plot graphs (y as a function of x)
ax.plot(x, K+0.05)


# Label and title the graph
ax.set(
    xlabel = "mole fraction of H$_{2}$O",
    ylabel = "reaction equilibrium",
    title = "reaction equilibrium vs mole fraction"
) 

ax.grid(True)
ax.legend(loc="best")

fig.tight_layout() #tighten layout

#save
fig.savefig('chapra_6_014_plot.png') 

#find roots
r1 = opt.brentq(lambda x: -0.05 + (x/(1-x)) * np.sqrt(6/(2+x)), 0.02, 0.04)
print(r1)
