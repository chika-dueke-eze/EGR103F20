"""
[extremes.py]
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
from mpl_toolkits.mplot3d import axes3d

#%% for chapra_7_025_plot
def f(x, y):
    return 2*y**2 - 2.25*x*y - 1.75*y + 1.5*x**2

min_loc = opt.fmin(lambda vec: f(vec[0], vec[1]), [0, 0])
print("7.025", min_loc)
min_val1 = f(*min_loc)

x1 = np.linspace(-4,4,20)
y1 = np.linspace(-4,4,20)

x1,y1 = np.meshgrid(x1,y1)
z1 = f(x1,y1)

fig = plt.figure(num=1, clear=True)
ax = fig.add_subplot(1,1,1, projection="3d")

ax.plot_wireframe(x1,y1,z1,color='purple')

ax.set(
       xlabel= "x",
       ylabel="y",
       zlabel="z",
       title = "chapra07.025 (cgd19)"
       )

fig.set_size_inches(6, 6, forward=True)
fig.tight_layout()

fig.savefig('chapra_7_025_plot.png')


#%% for chapra_7_026_plot.png
def f2(x, y):
    return -(4*x + 2*y + x**2 -2*x**4 + 6*x*y - 3*y**2)   #add minus sign since we're looking for max

def f2_main(x, y):
    return 4*x + 2*y + x**2 -2*x**4 + 6*x*y - 3*y**2

min_loc = opt.fmin(lambda vec: f2(vec[0], vec[1]), [0, 0])
print("7.026", min_loc)
max_val2 = f2_main(*min_loc)
print("max val for 7.026: ", max_val2)

x2 = np.linspace(-4,4,20)
y2 = np.linspace(-4,4,20)

x2,y2 = np.meshgrid(x2,y2)
z2 = f2_main(x2,y2)

fig = plt.figure(num=2, clear=True)
ax = fig.add_subplot(1,1,1, projection="3d")

ax.plot_wireframe(x2,y2,z2,color='orange')

ax.set(
       xlabel= "x",
       ylabel="y",
       zlabel="z",
       title = "chapra07.026 (cgd19)"
       )

fig.set_size_inches(6, 6, forward=True)
fig.tight_layout()

fig.savefig('chapra_7_026_plot.png')


#%% for chapra_7_027_plot.png
def f3(x, y):
    return -8*x + x**2 + 18*y + 4*y**2 -2*x*y 


min_loc = opt.fmin(lambda vec: f3(vec[0], vec[1]), [0, 0])
print("7.027", min_loc)
min_val3 = f3(*min_loc)


x3 = np.linspace(-4,4,20)
y3 = np.linspace(-4,4,20)

x3,y3 = np.meshgrid(x3,y3)
z3 = f3(x3,y3)

fig = plt.figure(num=3, clear=True)
ax = fig.add_subplot(1,1,1, projection="3d")

ax.plot_wireframe(x3,y3,z3,color='green')

ax.set(
       xlabel= "x",
       ylabel="y",
       zlabel="z",
       title = "chapra07.027 (cgd19)"
       )

fig.set_size_inches(6, 6, forward=True)
fig.tight_layout()

fig.savefig('chapra_7_027_plot.png')
