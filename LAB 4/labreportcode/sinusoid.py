# %% import modules
import numpy as np
import matplotlib.pyplot as plt

# %%
def y(t, A, omega, phi):
    return A*np.cos(omega * t + phi)
    
t = np.linspace(-2*np.pi, 2*np.pi, 101)         #get values for the independent variable 't' on the domain -2pi,2pi
y1 = y(t, 1, 1, 0)
y2 = y(t, 2, 1, 0)
y3 = y(t, 1, 2, 0)
y4 = y(t, 1, 1, np.pi/4)  

# Create a figure and axis
fig = plt.figure(num=1, clear=True)
ax = fig.add_subplot(1, 1, 1)

#plot the values
ax.plot(t, y1, 'b^-', mec='r', mfc='m', markevery=10, markersize=10)           
ax.plot(t, y2, 'ys--', mec='r', mfc='m', markevery=10, markersize=10)
ax.plot(t, y3, 'bp:', mec='c', mfc='m', markevery=10, markersize=10)
ax.plot(t, y4, 'bh-.', mec='r', mfc='m', markevery=10, markersize=10)
ax.legend(['$y(t, 1, 1, 0)$', '$y(t, 2, 1, 0)$', '$y(t, 1, 2, 0)$', 'y(t, 1, 1, $\dfrac{\pi}{4}$)'], loc='best')

# Turn the grid on
ax.grid(True)

# Use tight layout
fig.tight_layout()

# Save the graph as EPS and PDF
fig.savefig('SinusoidalFuction.pdf')
fig.savefig('SinusoidalFuction.eps')
