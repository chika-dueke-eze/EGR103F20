"""
[chapra_6_013.py]
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
T = np.linspace(0,1200,100)
cp =  -1.1 + 0.99403 + (1.671*(10**-4)*T) + (9.7215*(10**-8)*(T**2)) - (9.5838*(10**-11)*(T**3)) + (1.9520*(10**-14)*(T**4))

#%% initialize graph
fig, ax = plt.subplots(num=1, clear=True)
fig.set_size_inches(6, 4, forward=True)
 
#plot graphs (y as a function of x)
ax.plot(T, cp+1.1)


# Label and title the graph
ax.set(
    xlabel = "temperature, K",
    ylabel = "specific heat of dry air, kJ/(kg K)",
    title = "specific heat of dry air vs temperature "
) 

ax.grid(True)
ax.legend(loc="best")

fig.tight_layout() #tighten layout

#save
fig.savefig('chapra_6_013_plot.png') 

#find roots
r1 = opt.brentq(lambda T: -1.1 + 0.99403 + (1.671*(10**-4)*T) + (9.7215*(10**-8)*(T**2)) - (9.5838*(10**-11)*(T**3)) + (1.9520*(10**-14)*(T**4)), 0, 1000)
print(r1)
