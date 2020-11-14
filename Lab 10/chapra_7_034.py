"""
[chapra_7_034.py]
[Chika Dueke-Eze]
[11-14-2020]
Based on: pundit code
Written by: Michael R. Gustafson II

I understand and have adhered to all the tenets of the Duke Community Standard
in creating this code.
Signed: [chika]
"""
# %% Import modules
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

#%%calculating extremas
def maxtorque(s):
    return -((15*s)*(1-s))/((1-s)*(4*s**2 -3*s + 4))    #minus signs are generally cause of max

#using fminnboud
out1a = opt.fminbound(maxtorque, 0, 2)
print("{:.3e}".format(out1a))
max_val1 = -(maxtorque(out1a))        
print("fminbd max: ", max_val1)

#using fmin
min_loc = opt.fmin(lambda i: maxtorque(i[0]), [2])
max_val2 = -(maxtorque(*min_loc))
print("fmin max_val: = ", max_val2)
print("{:.3e}".format(min_loc[0]))
