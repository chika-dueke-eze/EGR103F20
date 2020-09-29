import math as m
import numpy as np


def calc_cos(x, es=0.0001, maxit=50):
    """
    Maclaurin series of exponential function
      sol, ea, it, sollist, ealist = iter_meth(x, es, maxit)
    input:
      x = value at which series evaluated
      es = stopping criterion (default = 0.0001)
      maxit = maximum iterations (default = 50)
    output:
      sol = estimated value
      ea = approximate relative error (%)
      it = number of iterations
      sollist = estimated values at each iteration
      ealist = approcimate relative error (%) at each iteration
    """

    # initialization
    it = 1
    sol = 1
    ea = 100
    sollist = [sol]
    ealist = [ea]

    # iterative calculation
    while True:
        solold = sol
        sol = sol + ((-1) ** it * (x ** (2*it))) / m.factorial(2*it)     #since cos function alternates signs we multiple by multiple by -1 for odd number iterations and +1 for even
        it = it + 1
        if sol != 0:
            ea = abs((sol - solold) / sol) * 100

        sollist += [sol]
        ealist += [ea]

        if ea <= es or it >= maxit:
            break

    return sol, ea, it, np.array(sollist), np.array(ealist)
