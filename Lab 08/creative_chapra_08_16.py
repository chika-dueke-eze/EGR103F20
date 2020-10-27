import numpy as np
import matplotlib.pyplot as plt
from chapra_08_16 import rotate_2d

x = np.array([1, 9, 9, 4, 1])
y = np.array([1, 1, 5, 5, 1])
plt.figure(1).clf()
fig, ax = plt.subplots(num=1)

for k in np.arange(0, 360, 6):
    x2, y2 = rotate_2d(k, x, y)
    ax.plot(x2, y2,
            color=[(1+np.cos(2*np.pi*k/360))/2,
                   (1+np.cos(2*np.pi*(k+120)/360))/2,
                   (1+np.cos(2*np.pi*(k+240)/360))/2])
ax.axis('equal')
fig.tight_layout()

fig.savefig('creativechapra.eps')
