'''
script that takes 2 parameters 'n' --> no of digits and 'm'--> int value
and returns the total number of factor in the interval
'''

def factor_count(n, m):
    small_n = 10**(n-1)      #gets the lower limit of the interval
    big_n = (10**n) - 1      #gets the upper limit of the interval
    poss_vals = (big_n//m)-(small_n//m)
    return poss_vals

if __name__ == "__main__":
    print(factor_count(1,4))
    print(factor_count(2,8))

