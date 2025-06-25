import math

# This function might be changed to the one you want to use
def punto_fijo(g, x0, e):
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

def g(x):
    return math.exp(x/4)

punto_fijo(g, 2, 10**-4)
