"""
[chapra_14_007.py]
[Chika Dueke-Eze]
[11-01-2020]
Based on: pundit code
Written by: Michael R. Gustafson II

I understand and have adhered to all the tenets of the Duke Community Standard
in creating this code.
Signed: chika
"""
# %% import modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from lab9_common import *

T = np.array([-40,0,40,80,120,160])  #values in celcius
T += 273 #convert to kelvin
p = np.array([6900,8100,9350,10500,11700,12800])
V = 10
n = 1000/28
Tmodel = np.linspace(T.min(),T.max(),100)

#%%perform calculations
def yfun(xe, coefs):
    return coefs[0] * xe**1 

Tv = np.reshape(T, (-1,1))
pv = np.reshape(p, (-1,1))
phi_mat = np.block([[Tv**1]])
pvec = np.linalg.lstsq(phi_mat, pv, rcond=None)[0]
print(pvec)

# %% Generate estimates and model
phat = yfun(T, pvec)
pmodel = yfun(Tmodel, pvec)

# %% Calculate statistics
calc_stats(p, phat, 1)

# %% Generate plots
make_plot(T, p, phat, Tmodel, pmodel)

# calculare R
R = pvec[0]*V/n
print("{:.4e}".format(R[0]))
