"""
Python version of Chapra Case Study 8.3 - Voltage sweep
From: Applied Numerical Methods with MATLAB
      for Engineers and Scientists, 4th ed
      Steven C. Chapra
      McGraw-Hill 2018
Edited by:
@Chika Dueke-Eze
"""
import numpy as np
import matplotlib.pyplot as plt

npts = 101
volt = np.linspace(0, 400, npts)
lst = []

for k in range(len(volt)):
    A = np.array([[1, 1,1,0,0,0], 
                  [0,-1,0,1,-1,0],
                  [0,0,-1,0,0,1],
                  [0,0,0,0,1,-1],
                  [0,10,-10,0,-15,-5],
                  [5,-10,0,-20,0,0]])
    b = np.array([
                  [0],
                  [0],
                  [0],
                  [0],
                  [0],
                  [volt[k]]
                  ])
    soln = np.linalg.solve(A, b)
    i_52 = soln[1][0]
    lst.append(i_52)
    
fig = plt.figure(num=1, clear=True)
ax = fig.add_subplot(1, 1, 1)
ax.plot(volt, lst, color='purple')
ax.set(xlabel='volt, V',
       ylabel = 'current, A'
      )
ax.grid(True)
ax.legend(loc='best')
fig.savefig('sweep1.eps')
