"""
[chapra_6_017.py]
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

w = 10
y0 = 5
y = 15
x = 50

#find roots
r1 = opt.fsolve(lambda Ta: -y + ((Ta/w)*np.cosh((w/Ta)*x)+y0-(Ta/w)), 1000)
print(r1)

#%% load values
w = 10
y0 = 5
Ta = r1

x = np.linspace(-50,100,100)
y = ((Ta/w)*np.cosh((w/Ta)*x)+y0-(Ta/w))

#%% initialize & plot graph
fig, ax = plt.subplots(num=1, clear=True)
fig.set_size_inches(6, 4, forward=True)
 
#plot graphs (y as a function of x)
ax.plot(x, y)


# Label and title the graph
ax.set(
    xlabel = "distance",
    ylabel = "height",
    title = "distance vs height"
) 

ax.grid(True)
ax.legend(loc="best")

fig.tight_layout() #tighten layout

#save
fig.savefig('chapra_6_017_plot.png') 
