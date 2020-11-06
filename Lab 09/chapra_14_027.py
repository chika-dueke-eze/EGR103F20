"""
[chapra_14_027.py]
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

V = np.array([2,3,4,5,7,10])
I = np.array([5.2,7.8,10.7,13,19.3,27.5])
Vmodel = np.linspace(V.min(),V.max(),100)

#%%#linear regression with polyfit (14.027b)
p = np.polyfit(V,I,1)
print("polyfit: {} ".format(p))

def polyfiteqn(p,x):              #function that takes input and returns output
    return p[0]*x + p[1]

#print("{:.3e}".format(polyfiteqn(p, 1)))
Imodel_1 = np.polyval(p,Vmodel)
Ihat_1 = np.polyval(p,V)
calc_stats(I,Ihat_1,1)
print("At 3.5V (polyfit): {:.3e}".format(np.polyval(p,3.5)))

#%%#linear regression with gen. linregr (14.027d)
#perform calculations

def yfun(xe, coefs):
    return coefs[0] * xe**1 

Vv = np.reshape(V, (-1,1))
Iv = np.reshape(I, (-1,1))
phi_mat = np.block([[Vv**1]])
pvec = np.linalg.lstsq(phi_mat, Iv, rcond=None)[0]
print("\n\npvec: {}".format(pvec[0]))

# %% Generate estimates and model
Ihat_2 = yfun(V, pvec)
Imodel_2 = yfun(Vmodel, pvec)
#print("14.027d: {:.3e}".format(yfun(2, pvec)[0]))                #answer to 14.027d
print("At 3.5V (genlin): {:.3e}".format(yfun(3.5, pvec)[0]))  

# %% Calculate statistics
calc_stats(I, Ihat_2, 1)

#%% initialize graph
fig, ax = plt.subplots(num=1, clear=True)
fig.set_size_inches(6, 4, forward=True)
 
#plot graphs (y as a function of x)
ax.plot(V, I, "ko", label="Data")
ax.plot(Vmodel, Imodel_1, "b-", label="Model", mfc="none")
ax.plot(Vmodel, Imodel_2, "r--", label="Model")
ax.grid(True)
ax.legend(loc="best")

ax.set(
    xlabel = "V, v",
    ylabel = "i, A",
) 

fig.tight_layout() #tighten layout

#save
fig.savefig('chapra_14_027_plot.png')
