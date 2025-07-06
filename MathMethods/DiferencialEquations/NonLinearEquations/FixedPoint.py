import math

# Modify this parameters and functions for your case
x_0 = 2
eTolerance = 10**-4
def g(x):
    return math.exp(x/4)

def fixed_point(g, x0, e):
    x = [x0]
    error = 1
    k = 1
    print("Iteration\tAproximation\tError")
    while error > e:
        xk = g(x[k-1])
        x.append(xk)
        error = abs(x[k] - x[k-1])
        print("{}\t\t{:.8f}\t{:.8f}".format(k, xk, error))
        k += 1
    print("Number of iterations:", k)

fixed_point(g, x_0, eTolerance)
