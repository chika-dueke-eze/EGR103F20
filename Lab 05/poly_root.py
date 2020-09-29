def calc_root(x, es=0.0001, maxit=50):
    # initialization
    it = 1
    sol = x
    ea = 100

    # iterative calculation
    while True:
        solold = sol
        sol = (2*x**3-7*x**2+ 8) / (3*x**2-14*x+14)
        x = sol
        it = it + 1
        if sol != 0:
            ea = abs((sol - solold) / sol) * 100

        if ea <= es or it >= maxit:
            break

    return sol, ea, it

if __name__ == "__main__":
    print(calc_root(0))
