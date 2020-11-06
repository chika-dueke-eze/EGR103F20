"""
[chapra_15_005.py]
[Chika Dueke-Eze]
[11-01-2020]
Based on: pundit code
Written by: Michael R. Gustafson II

I understand and have adhered to all the tenets of the Duke Community Standard
in creating this code.
Signed: chika
"""
# %% import modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from lab9_common import *

#%% load and manipulate data
t = np.array([0,5,10,15,20,25,30])
c = np.array([14.6,12.8,11.3,10.1,9.09,8.26,7.56])
tmodel = np.linspace(t.min(),t.max(),100)
#%%perform calculations
def yfun(xe, coefs):
    return coefs[0] * xe**3 + coefs[1]*xe**2 + coefs[2]*xe**1 + coefs[3]*xe**0

tv = np.reshape(t, (-1,1))
cv = np.reshape(c, (-1,1))
phi_mat = np.block([[tv**3,tv**2,tv**1,tv**0]])
pvec = np.linalg.lstsq(phi_mat, cv, rcond=None)[0]
print(pvec)

# %% Generate estimates and model
chat = yfun(t, pvec)
cmodel = yfun(tmodel, pvec)

# %% Calculate statistics
calc_stats(c, chat, 1)


#%% initialize graph
fig, ax = plt.subplots(num=1, clear=True)
fig.set_size_inches(6, 4, forward=True)
 
#plot graphs (y as a function of x)
ax.plot(t, c, "ko", label="Data")
ax.plot(tmodel, cmodel, "-", label="Model", mfc="none")


# Label and title the graph
ax.set(
    xlabel = "t, temp ($\degree C$)",
    ylabel = "Dissolved Oxygen (mg/L)",
    title = "Dissolved Oxygen vs Temp (cgd19 )",
) 
ax.grid(True)
ax.legend(loc="best")

fig.tight_layout() #tighten layout

#save
fig.savefig('chapra_15_005_plot.png')
