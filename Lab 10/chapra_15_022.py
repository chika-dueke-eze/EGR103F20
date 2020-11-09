"""
[chapra_15_022.py]
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
x = np.array([0.5,1,2,3,4])
y = np.array([10.4,5.8,3.3,2.4,2])
xmodel = np.linspace(x.min(), x.max(), 100)


# %% Perform calculations
def yfun(x, *coefs):
    return ((coefs[0] + np.sqrt(x))/(coefs[1] * np.sqrt(x)))**2

popt = opt.curve_fit(yfun, x, y, [1,1])[0]
print("{:.3e}".format(popt[0]))
print("{:.3e}".format(popt[1]))

#when x= 1.6
print("y when x = 1.6 is ", yfun(1.6, *popt))

# %% Generate estimates and model
yhat = yfun(x, *popt)
ymodel = yfun(xmodel, *popt)

# %% Calculate statistics
calc_stats(y, yhat, 1)

#%% initialize graph
fig, ax = plt.subplots(num=1, clear=True)
fig.set_size_inches(6, 4, forward=True)
 
#plot graphs (y as a function of x)
ax.plot(x, y, "ms", label="Data")
ax.plot(xmodel, ymodel, "y-", label="Model", mfc="none")


# Label and title the graph
ax.set(
    xlabel = "x",
    ylabel = "y ",
) 
ax.grid(True)
ax.legend(loc="best")

fig.tight_layout() #tighten layout

#save
fig.savefig('chapra_15_022_plot.png')
