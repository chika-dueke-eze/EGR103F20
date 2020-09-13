# -*- coding: utf-8 -*-
"""
[keep_time.py]
[Chika Dueke-Eze]
[09-04-2020]

I understand and have adhered to all the tenets of the Duke Community Standard
in creating this code.
Signed: [cgd19]
"""


def bounded(x, low=0, high=2.375):  
    x = float(x)
    if x <= low:
        return low
    elif low<x<high:
        return x
    else:
        return high

if __name__ == "__main__":
    a = 4
    a = bounded(a)
    print(a)


    
##    for k in range(-2, 5):
##        #print(bounded(k, 0.5, 2.5))
##        print(bounded(k))  # uncomment once defaults included


        
