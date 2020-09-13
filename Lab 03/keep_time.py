# -*- coding: utf-8 -*-
"""
[keep_time.py]
[Chika Dueke-Eze]
[09-04-2020]

I understand and have adhered to all the tenets of the Duke Community Standard
in creating this code.
Signed: [cgd19]
"""


# %% Define function
def hms(seconds):
    hrs = seconds//3600               #to find no of hours in the seconds
    mins = (seconds % 3600)//60       #to find no of minutes in the seconds
    secs = (seconds % 3600) % 60      #to find the remaining seconds
    return (hrs,mins,secs)


if __name__ == "__main__":
    print(hms(0))
    print(hms(1))
    print(hms(60))
    print(hms(3600))
