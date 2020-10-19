import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

rho = 1
phi, theta = np.meshgrid(np.linspace(0,np.pi,20), 
                  np.linspace(0,2*np.pi,40))

x = rho * np.sin(phi) * np.cos(theta)
y = rho * np.sin(phi) * np.sin(theta)
z = rho * np.cos(phi)

fig = plt.figure(num=1, clear=True)
ax = fig.add_subplot(1,1,1, projection="3d")

ax.plot_wireframe(x,y,z,color='purple')

ax.set(
       xlabel= "x",
       ylabel="y",
       zlabel="z",
       xticks = [-1,0,1],
       yticks = [-1,0,1],
       zticks = [-1,0,1]
       
       )

fig.set_size_inches(6, 6, forward=True)
fig.tight_layout()

fig.savefig('sphere_plot.eps')
