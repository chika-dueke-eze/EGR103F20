"""
[chapra_14_005.py]
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

x = np.array([0,2,4,6,9,11,12,15,17,19])
y = np.array([5,6,7,6,9,8,8,10,12,12])

n = len(y)

#%% y as a function of x
p1 = np.polyfit(x,y,1)
print(p1)

xmodel = np.linspace(x.min(),x.max(),100)

yhat = np.polyval(p1,x)
ymodel = np.polyval(p1,xmodel)

st_1,sr_1,r2_1 = calc_stats(y,yhat)
r1 = np.sqrt(r2_1)
print("r: {:.3e}".format(r1))

stderror1 = np.sqrt((sr_1/(n-2)))
print("stderror: {:.3e} \n\n".format(stderror1))

#%%  x as a function of y

p2 = np.polyfit(y,x,1)
print(p2)

ymodel = np.linspace(y.min(),y.max(),100)

xhat = np.polyval(p2,y)
xmodel = np.polyval(p2,ymodel)

st_2,sr_2,r2_2 = calc_stats(x,xhat)
r2 = np.sqrt(r2_2)
print("r: {:.3e}".format(r2))

stderror1 = np.sqrt((sr_2/(n-2)))
print("stderror: {:.3e}".format(stderror1))

#%% initialize graph
fig, ax = plt.subplots(2,1,num=1, clear=True)
fig.set_size_inches(6, 4, forward=True)
 
#plot graphs (y as a function of x)
ax[0].plot(x, y, "ko", label="Data")
ax[0].plot(x, yhat, "ks", label="Estimates", mfc="none")
ax[0].plot(xmodel, ymodel, "k-", label="Model")
ax[0].grid(True)
ax[0].legend(loc="best")

ax[0].set(
    xlabel = "x",
    ylabel = "y",
) 

#(x as a function of y)
ax[1].plot(y, x, "ko", label="Data")
ax[1].plot(y, xhat, "ks", label="Estimates", mfc="none")
ax[1].plot(ymodel, xmodel, "k-", label="Model")
ax[1].grid(True)
ax[1].legend(loc="best")

ax[1].set(
    xlabel = "y",
    ylabel = "x",
) 

fig.tight_layout() #tighten layout

#save
fig.savefig('chapra_14_005_plot.png')
