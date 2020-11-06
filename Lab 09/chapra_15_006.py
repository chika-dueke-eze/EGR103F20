"""
[chapra_15_006.py]
[Chika Dueke-Eze]
[11-01-2020]
Based on: pundit code
Written by: Michael R. Gustafson II

I understand and have adhered to all the tenets of the Duke Community Standard
in creating this code.
Signed: chika
"""
#%%
from lab9_common import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
import numpy as np

#%%
data = np.loadtxt("chapra_p15_5.dat")

c = data[:,0].copy()
t = data[:,1].copy()
o = data[:,2].copy()

cmodelm, tmodelm = np.meshgrid(np.linspace(min(c),max(c),7), np.linspace(min(t),max(t),19))

#%%
def zfun(xe, ye, coefs):
    return (coefs[0] * xe**0 + coefs[1] * xe + coefs[2] * ye)


# Reshape data for block matrices
xv = np.reshape(c, (-1, 1))
yv = np.reshape(t, (-1, 1))
zv = np.reshape(o, (-1, 1))
xm = np.reshape(c, (7, 3))
ym = np.reshape(t, (7, 3))
zm = np.reshape(o, (7, 3))
phi_mat = np.block([[xv**0, xv, yv]])
pvec = np.linalg.lstsq(phi_mat, zv, rcond=None)[0]
print(pvec)


# %% Generate estimates and model
zhatv = zfun(xv, yv, pvec) # for stats
zhatm = zfun(xm, ym, pvec) # for graphics
zmodelm = zfun(cmodelm, tmodelm, pvec)


eqn = zfun(15,12,pvec)
print(eqn)

print("%error: {:.2e}".format(100*((eqn[0]-9.09)/9.09)))

# %% Calculate statistics
calc_stats(zv, zhatv, 1)

# %% Generate plots
# Make model plot
fig = plt.figure(num=1, clear=True)
ax = fig.add_subplot(1, 1, 1, projection='3d')

surfhandle = ax.plot_surface(cmodelm, tmodelm, zmodelm, cmap=cm.winter)
#ax.scatter(cmodelm, tmodelm, zmodelm)
ax.set(
       xlabel= "C, g/L",
       ylabel="T, $\degree C$",
       zlabel="OC, mg/L",
       xticks = [0,10,20],
       yticks = [0,5,10,15,20,25,30]
       )
ax.view_init(elev=31, azim=46)    #for optimized view
fig.colorbar(surfhandle)
fig.tight_layout()
fig.savefig('chapra_15_006_plot1.png')

# Make error plot
fig = plt.figure(num=2, clear=True)
ax = fig.add_subplot(1, 1, 1, projection='3d')

sh = ax.plot_surface(xm, ym, zm-zhatm, cmap=cm.autumn)
ax.set(
       xlabel= "C, g/L",
       ylabel="T, $\degree C$",
       zlabel="Residual, mg/L",
       xticks = [0,10,20],
       yticks = [0,5,10,15,20,25,30]
       )
fig.colorbar(sh)
fig.tight_layout()
fig.savefig('chapra_15_006_plot2.png')
