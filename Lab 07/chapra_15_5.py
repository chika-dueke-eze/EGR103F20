import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm

data = np.loadtxt("chapra_p15_5.dat.txt")
c = data[:,0].copy()
T = data[:,1].copy()
OC = data[:,2].copy()

c = c.reshape(7,3)
T = T.reshape(7,3)
OC = OC.reshape(7,3)

fig = plt.figure(num=1, clear=True)
ax = fig.add_subplot(1,1,1, projection="3d")

#c,T = np.meshgrid(c,T)
plot = ax.plot_surface(c,T, OC, cmap=cm.winter)
fig.colorbar(plot) 

ax.set(
       xlabel= "Concentration of Chloride, g/L",
       ylabel="Temperature, degrees C",
       zlabel="Concentration of Oxyen, mg/L",
       xticks = [0,10,20],
       yticks = [0,5,10,15,20,25,30]
       )
ax.view_init(elev=32, azim=50)

fig.set_size_inches(6, 4, forward=True)
fig.tight_layout()

fig.savefig('chapra_15_05_plot.eps')
