"""
[chapra_15_011.py]
[Chika Dueke-Eze]
[11-08-2020]
Based on: pundit code
Written by: Michael R. Gustafson II

I understand and have adhered to all the tenets of the Duke Community Standard
in creating this code.
Signed: chika
"""
# %% Import modules
import numpy as np
from fitting_common import *
import scipy.optimize as opt

# %% Load and manipulate data
I = np.array([50,80,130,200,250,350,450,550,700])
P = np.array([99,177,202,248,229,219,173,142,72])
Imodel = np.linspace(I.min(), I.max(), 100)


# %% Perform calculations
def yfun(x, *coefs):
    return (coefs[0] * (x/coefs[1])) * np.exp((-x/coefs[1]+1))


popt = opt.curve_fit(yfun, I, P, [240, 250])[0]
print(popt)


# %% Generate estimates and model
Phat = yfun(I, *popt)
Pmodel = yfun(Imodel, *popt)

# %% Calculate statistics
calc_stats(P, Phat, 1)

#%% initialize graph
fig, ax = plt.subplots(num=1, clear=True)
fig.set_size_inches(6, 4, forward=True)
 
#plot graphs (y as a function of x)
ax.plot(I, P, "rd", label="Data")
ax.plot(Imodel, Pmodel, "g-", label="Model", mfc="none")


# Label and title the graph
ax.set(
    xlabel = "I, Solar Radiation ($μE m^{−2}s^{−1}$)",
    ylabel = "P, Photosynthesis Rate ($mg~m^{−3}d^{−1}$) ",
) 
ax.grid(True)
ax.legend(loc="best")

fig.tight_layout() #tighten layout

#save
fig.savefig('chapra_15_011_plot.png')
