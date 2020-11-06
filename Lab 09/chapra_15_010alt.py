"""
[chapra_15_010alt.py]
[Chika Dueke-Eze]
[11-01-2020]
Based on: pundit code
Written by: Michael R. Gustafson II

I understand and have adhered to all the tenets of the Duke Community Standard
in creating this code.
Signed: cgd19
"""
# %% import modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from lab9_common import *

t = np.array([0.5,1,2,3,4,5,6,7,9])
p = np.array([6,4.4,3.2,2.7,2,1.9,1.7,1.4,1.1])
tmodel = np.linspace(t.min(),t.max(),100)

# %% Perform calculations
def yfun(xe, coefs):
    return coefs[0] * np.exp(-1.5*xe) + coefs[1] * np.exp(-0.3*xe) + coefs[2] * np.exp(-0.2*xe)


# Reshape data for block matrices
tv = np.reshape(t, (-1, 1))
pv = np.reshape(p, (-1, 1))
phi_mat = np.block([[np.exp(-1.5*tv), np.exp(-0.3*tv), np.exp(-0.2*tv)]])
pvec = np.linalg.lstsq(phi_mat, pv, rcond=None)[0]
print(pvec)

A = pvec[0][0]
B = pvec[1][0]
C = pvec[2][0]
# %% Generate estimates and model
phat = yfun(t, pvec)
pmodel = yfun(tmodel, pvec)

# %% Calculate statistics
calc_stats(p, phat, 1)


#%% initialize graph
fig, ax = plt.subplots(num=1, clear=True)
fig.set_size_inches(6, 4, forward=True)
 
#plot graphs (y as a function of x)
ax.plot(t, p, "mo", label="Data")
ax.plot(tmodel, pmodel, "k-", label="Model", mfc="none")
ax.plot(t,A*np.exp(-1.5*t), "b--", label="A")
ax.plot(t,B*np.exp(-0.3*t),  "g--", label="B")
ax.plot(t,C*np.exp(-0.2*t),  "r--", label="C")

# Label and title the graph
ax.set(
    xlabel = "t, days",
    ylabel = "concentration, organism/$cm^3$",
    title = "Concentration vs Time (cgd19 )",
) 
ax.grid(True)
ax.legend(loc="best")

fig.tight_layout() #tighten layout

#save
fig.savefig('chapra_15_010alt_plot.png')
