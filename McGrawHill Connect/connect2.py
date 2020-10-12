# -*- coding: utf-8 -*-
"""
SCRIPT FOR SOLVING PROBLEM 02.021
"""
#%%
import numpy as np
import matplotlib.pyplot as plt


m = np.array([83.6,60.2,72.1,91.1,92.9,65.3,80.9])
v_t = np.array([53.4,48.5,50.9,55.7,54,47.7,51.1])
A = np.array([0.455,0.402,0.452,0.486,0.531,0.475,0.487])
g = 9.8
p = 1.103

C_D = (2 * m * g)/(v_t**2 * p * A)


CDlst = []
for i in C_D:
    val = "{:.4f}".format(i)
    CDlst.append(float(val))

print(CDlst)


print("min: {:.4f}".format(C_D.min()))
print("max: {:.4f}".format(C_D.max()))
print("avg: {:.4f}".format(C_D.mean()))

fig, ax = plt.subplots(2, 1, num=1, clear=True)


#plot graph of A versus m
ax[0].plot(m,A, '.')
ax[0].grid(True)
ax[0].set(
    #xlabel = "m, kg",
    ylabel = "A, m^2",
    title = "A versus m"
    )

#plot graph of C_D versus m
ax[1].plot(m,C_D, '.')
ax[1].grid(True)
ax[1].set(
    xlabel = "m, kg",
    ylabel = "C_D, **",
    title = "C_D versus m"
    )

fig.savefig("connect02021.png")
