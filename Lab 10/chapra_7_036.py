"""
[chapra_7_036.py]
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
def rollbear(x):
    return -((0.3/np.sqrt(1+x**2))-(np.sqrt(1+x**2)*(1-(0.3/(1+x**2)))) + x)    #minus signs are generally cause of max

#using fminnboud
out1a = opt.fminbound(rollbear, 0, 4)
print("{:.3e}".format(out1a))
max_val1 = -(rollbear(out1a))        
print("fminbd max: ", max_val1)

#using fmin
min_loc = opt.fmin(lambda i: rollbear(i[0]), [2])
max_val2 = -(rollbear(*min_loc))
print("fmin max_val: = ", max_val2)
print("{:.3e}".format(min_loc[0]))
