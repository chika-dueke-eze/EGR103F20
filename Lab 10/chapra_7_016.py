"""
[chapra_7_016.py]
[Chika Dueke-Eze]
[11-14-2020]
Based on: pundit code
Written by: Michael R. Gustafson II

I understand and have adhered to all the tenets of the Duke Community Standard
in creating this code.
Signed: [chika]
"""
# %% Import modules
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

#%%
ri = np.linspace(1/1000,12/1000,100)
T = 293 + (75/(2*np.pi)) * ( ((1/0.17)*np.log((0.006+ri)/0.006)) + ((1/12)*(1/(0.006+ri))))

#%% initialize graph
fig, ax = plt.subplots(num=1, clear=True)
fig.set_size_inches(6, 4, forward=True)
 
#plot graphs (y as a function of x)
ax.plot(ri, T)


# Label and title the graph
ax.set(
    xlabel = "Insulation Thickness, m",
    ylabel = "Temperature, K",
    title = "Temperature (K) vs Insulation Thickness (m)"
) 
ax.grid(True)
ax.legend(loc="best")

fig.tight_layout() #tighten layout

#save
fig.savefig('chapra_7_016_plot.png')

#%%calculating extremas
def mintemp(ri):
    return  293 + (75/(2*np.pi)) * ( ((1/0.17)*np.log((0.006+ri)/0.006)) + ((1/12)*(1/(0.006+ri))))

#using fminnboud
out1a = opt.fminbound(mintemp, 0.006, 0.010)
out1a *= 1000     #convert to mm
print("fminbound thickness: {:.3e}".format(out1a))
print("fminbound temp: {:.3e}".format(mintemp(out1a/1000)))


#using fmin
min_loc = opt.fmin(lambda i: mintemp(i[0]), [0.010])
min_val = mintemp(*min_loc)
min_loc *= 1000      #convert to mm
print("fmin thickness {:.3e}".format(min_loc[0]))
