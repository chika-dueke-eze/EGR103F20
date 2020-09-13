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
def total_seconds(hrs, mins=0, secs=0): 
    sec_1 = hrs * 3600
    sec_2 = mins * 60
    sec_3 = secs
    total_sec = sec_1 + sec_2 + sec_3
    return total_sec


if __name__ == "__main__":
    print(total_seconds(1))
    print(total_seconds(1, 2))
    print(total_seconds(1, 2, 3))
    print(total_seconds(1, secs=3))
