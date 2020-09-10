def factor_count(n, m):
    small_n = 10**(n-1)
    big_n = (10**n) - 1
    poss_vals = (big_n//m)-(small_n//m)
    return poss_vals

if __name__ == "__main__":
    print(factor_count(1,4))
    print(factor_count(2,8))

