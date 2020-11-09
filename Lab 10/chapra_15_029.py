"""
[chapra_15_029.py]
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
T = np.array([50,60,70,80,90,100,110,120,130])
P = np.array([82,2300,18500,80500,230000,500000,960000, 1500000,2400000])
y = np.log(P)
Tmodel = np.linspace(T.min(), T.max(), 100)


# %% Perform calculations
def yfun(x, *coefs):
    return coefs[0] - (coefs[1]/(coefs[2]+x))

popt = opt.curve_fit(yfun, T, y, [100, 10,20])[0]
print("{:.3e}".format(popt[0]))
print("{:.3e}".format(popt[1]))
print("{:.3e}".format(popt[2]))


# %% Generate estimates and model
yhat = yfun(T, *popt)
ymodel = yfun(Tmodel, *popt)

# %% Calculate statistics
stats = calc_stats(y, yhat, 1)
s_yx = np.sqrt(stats[1]/(len(T)-3))
print("s_y/x = {:.3e}".format(s_yx))


#%% initialize graph
fig, ax = plt.subplots(num=1, clear=True)
fig.set_size_inches(6, 4, forward=True)
 
#plot graphs (y as a function of x)
ax.plot(T, y, "ms", label="Data")
ax.plot(Tmodel, ymodel, "y-", label="Model", mfc="none")


# Label and title the graph
ax.set(
    xlabel = "x",
    ylabel = "y ",
) 
ax.grid(True)
ax.legend(loc="best")

fig.tight_layout() #tighten layout

#save
fig.savefig('chapra_15_029_plot.png')
