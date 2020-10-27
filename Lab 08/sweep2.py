
"""
Python version of Chapra Case Study 8.3 - Resistance sweep
From: Applied Numerical Methods with MATLAB
      for Engineers and Scientists, 4th ed
      Steven C. Chapra
      McGraw-Hill 2018
Edited by:
@Chika Dueke-Eze
"""

import numpy as np
import matplotlib.pyplot as plt

npts = 201
r = np.linspace(0, 100, npts)
current = []
cond_no = []
for k in range(len(r)):
    A = np.array([[1, 1,1,0,0,0], 
                  [0,-1,0,1,-1,0],
                  [0,0,-1,0,0,1],
                  [0,0,0,0,1,-1],
                  [0,r[k],-10,0,-15,-5],
                  [5,-r[k],0,-20,0,0]])
    b = np.array([
                  [0],
                  [0],
                  [0],
                  [0],
                  [0],
                  [200]
                  ])
    
    soln = np.linalg.solve(A, b)
    i_52 = soln[1][0]
    cond = np.linalg.cond(A,2)
    cond = np.log10(cond)
    current.append(i_52)
    cond_no.append(cond)

#plot current against resistance
fig1 = plt.figure(num=1, clear=True)
ax1 = fig1.add_subplot(1, 1, 1)
ax1.plot(r, current, color='orange')
ax1.set(xlabel='resistance, $\Omega$',
        ylabel = 'current, A',
        title = "Current VS Resistance"
      )
ax1.grid(True)
ax1.legend(loc='best')


#plot log10cond against resistance
fig2 = plt.figure(num=2, clear=True)
ax2 = fig2.add_subplot(1, 1, 1)
ax2.plot(r, cond_no, color='black')
ax2.set(xlabel='resistance, $\Omega$',
       ylabel = 'Log10 Condition number',
       title = "Base-10 Logarithm of Condition Number VS Resistance"
      )
ax2.grid(True)
ax2.legend(loc='best')

#save figs
fig1.savefig('cVSr.eps')
fig2.savefig('condlogVSVSr.eps')
