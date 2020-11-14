"""
[chapra_7_031.py]
[Chika Dueke-Eze]
[11-14-2020]
Based on: pundit code
Written by: Michael R. Gustafson II

I understand and have adhered to all the tenets of the Duke Community Standard
in creating this code.
Signed: [cdg19]
"""
# %% Import modules
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

#%% load values
t = np.linspace(0,20,100)
o = 10 - ((0.1*30)/(0.1+0.05-0.6)*(np.exp(-0.6*t)-np.exp(-(0.1+0.05)*t))) - ((1/0.6)*(1-np.exp(-0.6*t)))

#%% initialize graph
fig, ax = plt.subplots(num=1, clear=True)
fig.set_size_inches(6, 4, forward=True)
 
#plot graphs (y as a function of x)
ax.plot(t, o)


# Label and title the graph
ax.set(
    xlabel = "travel time, d",
    ylabel = "dissolved oxygen concentration, mg/L",
    title = "dissolved oxygen concentration (mg/L) vs travel time (d)"
) 
ax.grid(True)
ax.legend(loc="best")

fig.tight_layout() #tighten layout

#save
fig.savefig('chapra_7_031_plot.png')

#%%calculating extremas
def crit_conc(t):
    return  10 - ((0.1*30)/(0.1+0.05-0.6)*(np.exp(-0.6*t)-np.exp(-(0.1+0.05)*t))) - ((1/0.6)*(1-np.exp(-0.6*t)))

#using fminnboud
out1a = opt.fminbound(crit_conc, 2.5, 5, full_output=True)
print("{:.3e} {:.3e}".format(out1a[0], out1a[1]))

#using fmin
min_loc = opt.fmin(lambda i: crit_conc(i[0]), [4])
min_val = crit_conc(*min_loc)
print("{:.3e}".format(min_loc[0]))
