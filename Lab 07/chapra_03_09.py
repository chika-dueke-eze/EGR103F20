#%%
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm

#assign values to variables
n = 0.02
S = 0.001
B = np.linspace(0.01,20,40)
H = np.linspace(0.01,5,41)

B, H = np.meshgrid(B, H)   #use meshgrid to create array of similar size
U = np.sqrt(S)/n * (B*H/(B + 2*H))**(2/3)

#start plottting
fig = plt.figure(num=1, clear=True)
ax = fig.add_subplot(1,1,1, projection="3d")

plot = ax.plot_surface(B,H,U, cmap=cm.autumn)      #plot the surface and use a color map
fig.colorbar(plot)       #assign a color bar
 
ax.set(
       title = "Velocity using Manning's Equation",
       xlabel= "Width B, m",
       ylabel="Height H, m",
       zlabel="Velocity U, m/s",
       xticks = [0,5,10,15,20],
       yticks = [0,1,2,3,4,5],
       zticks = [0,0.5,1,1.5,2,2.5,3,3.5]
       )
ax.view_init(elev=35, azim=-135)    #for optimized view

fig.set_size_inches(6, 4, forward=True)
fig.tight_layout()

fig.savefig('chapra_03_09_plot.eps')
