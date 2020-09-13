# -*- coding: utf-8 -*-
"""
[tri_calc.py]
[Chika Dueke-Eze]
[09-13-2020]

I understand and have adhered to all the tenets of the Duke Community Standard
in creating this code.
Signed: [cgd19]
"""
# %% Import modules
import numpy as np
import matplotlib.pyplot as plt

# %% Define function


def triangles(a, b, c, draw=False, fnum=1):
    # %% Calculate angles
    A = np.arccos((b**2+c**2-a**2)/(2*b*c))
    B = np.arccos((a**2+c**2-b**2)/(2*a*c))
    C = np.arccos((a**2+b**2-c**2)/(2*a*b))
    # %% Make plot if asked
    if draw:
        fig = plt.figure(num=fnum, clear=True)
        ax = fig.add_subplot(1, 1, 1)

        # Calculations and plots
        #p3y = b * np.math.sin(C)    initially tried using trig to solve but didn't work out too well
        #p3x = b * np.math.cos(C)
        p3x = (c**2 - b**2 + 9)/6      #so I used transitioned to the more natural simulataneous equation
        p3y = np.sqrt(c**2 - p3x**2)
        px = [0,a]
        py = [0,0]
        
        ax.plot(px,py,'r-')                #connect first two point
        ax.plot([0,p3x], [0,p3y], 'r-')    #connect origin to third coordinate
        ax.plot([a,p3x], [0,p3y], 'r-')    # connect (a,0) to third coordinate
        
        ax.axis("equal")
        fig.tight_layout()

    # %% Return angles
    return A, B, C


if __name__ == "__main__":
    print(triangles(3, 6, 4, True, 5))
    print(triangles(5, 7, 9, True, 4))
    print(triangles(3, 4, 5, True, 1))
