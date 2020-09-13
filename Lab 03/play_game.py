# -*- coding: utf-8 -*-
"""
[Function or Script Name]
[Your Name]
[Date Modified]

I understand and have adhered to all the tenets of the Duke Community Standard 
in creating this code.
Signed: [Your NetID]
"""
# %% Import modules
import numpy as np


# %% Define function
def roll_dice(n_dice=1, n_sides=6, seed=0):     #define a function with parms for no of dice thrown, no of sides and seed (useful for random no generation)
    np.random.seed(seed)
    roll_vals = np.random.randint(1,n_sides+1,n_dice)   #use random.randint method to generate values
    
    roll_count = np.zeros(n_sides)          #this is used to create an array of 0's used to map values from the random sequence generated to their no of occurrence
    for count in roll_vals:
        roll_count[count-1] += 1

    return roll_vals, roll_count


if __name__ == "__main__":
    print(roll_dice(10, 6))
    roll_list, roll_count = roll_dice(5,6)
    print(roll_list, roll_count)
