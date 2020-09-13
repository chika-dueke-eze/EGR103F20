# -*- coding: utf-8 -*-
"""
[Function or Script Name]
[Your Name]
[Date Modified]

I understand and have adhered to all the tenets of the Duke Community Standard 
in creating this code.
Signed: [Your NetID]
"""
# %% Imports
from football_helper import bounded

# %% Define function
def you_shall_pass(pa, pc, py, td, intr):
    a = ((pc/pa)-0.3)*5
    a = bounded(a)          #to limit the function to interals of 0,2.375
    b = ((py/pa)-3)*0.25
    b = bounded(b)
    c = (td/pa)*20
    c = bounded(c)
    d = 2.375-((intr/pa)*25)
    d = bounded(d)
    
    rating = ((a+b+c+d)/6)*100
    rating = round(rating, 1)
    return rating


if __name__ == "__main__":
    print(you_shall_pass(30, 20, 286, 3, 0))
