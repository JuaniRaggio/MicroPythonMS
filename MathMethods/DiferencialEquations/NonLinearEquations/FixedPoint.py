import math

DD = 4

# Modify this parameters and functions for your case
x_0 = 2
h = 10**-4

def g(x):
    return math.exp(x/4)


def derivative_approx(g, x, h=1e-5):
    return (g(x + h) - g(x - h)) / (2 * h)

def verify_convergence(g, x0, h=1e-5):
    g_prime = derivative_approx(g, x0, h)
    print("g'(x0) =", g_prime)
    if abs(g_prime) < 1:
        print("Fixed point probably converges in x0 =", x0)
        return True
    else:
        print("Fixed point probably doesn't converge in x0 =", x0)
        return False

verify_convergence(g, x_0, h)

def fixed_point(g, x0, e):
    x = [x0]
    error = 1
    k = 1
    print("Iter\tAprox\tError")
    while error > e:
        xk = g(x[k-1])
        x.append(xk)
        error = abs(x[k] - x[k-1])
        print(k, "\t", round(xk, DD), "\t", round(error, DD))
        k += 1
    print("Number of iterations:", k)

fixed_point(g, x_0, h)
