# -*- coding: utf-8 -*-
"""
SCRIPT FOR SOLVING PROBLEM 03.001
"""
#%%
import numpy as np

#%%

def calc_vol(d,R):
    cyl_h = d - R
    
    if d <= R:
        cone_vol = (1/3) * (np.pi * R**2 * d)
        total_vol = ("{:.4f}".format(cone_vol))
        return(total_vol)
        
    elif d <= (3*R):
        cone_vol = (1/3) * (np.pi * R**2 * R)
        cyl_vol = (np.pi * R**2 * cyl_h)
        total_vol = cone_vol + cyl_vol
        total_vol = ("{:.4f}".format(total_vol))
        return(total_vol)
    
    else:
        return("Overtop")
    

if __name__ == "__main__":
    print(calc_vol(3.8, 1.4))
