import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

t = np.arange(0,6*np.pi, np.pi/64)  #get values between 0 and 6pi with increment of pi/64
x = t * np.cos(6*t)
y = t * np.sin(6*t)
z = t

fig = plt.figure(num=1, clear=True)

#plot bottom plot
ax1 = fig.add_subplot(2,1,1)
ax1.set(
       xlabel= "x",
       ylabel="y",
       )
ax1.plot(x,y,'r-')
ax1.axis('equal')
ax1.grid(True)


#plot bottom plot
ax2 = fig.add_subplot(2,1,2, projection="3d")
ax2.set(
       xlabel= "x",
       ylabel="y",
       zlabel="z",
       zlim = [0, 20],
       xticks = [-20, 0, 20],
       yticks = [-20, 0, 20],
       zticks = [0, 10, 20]
       )
ax2.plot(x,y,z,'c-')
#ax2.grid(True)

fig.set_size_inches(6, 8, forward=True)
fig.tight_layout()

fig.savefig('chapra_02_22_plot.eps')
