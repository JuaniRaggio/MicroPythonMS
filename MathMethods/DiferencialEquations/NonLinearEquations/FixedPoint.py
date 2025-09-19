import math

DD = 4

# Modify this parameters and functions for your case
x_0 = 2
h = 10**-4

def g(x):
    return math.exp(x/4)

def await_if_4(n):
    if n % 4 == 0 and n != 0:
        input("Enter to continue")

def derivative_approx(g, x, h):
    return (g(x + h) - g(x - h)) / (2 * h)

def verify_convergence(g, x0, h):
    g_prime = derivative_approx(g, x0, h)
    print("g'(x0) =", g_prime)
    if abs(g_prime) < 1:
        print("Fixed point probably converges in x0 =", x0)
        return True
    else:
        print("Fixed point probably doesn't converge in x0 =", x0)
        return False

verify_convergence(g, x_0, h)

input("Enter to continue")

def fixed_point(g, x0, e):
    x = [x0]
    error = 1
    k = 1
    print("Iter  Aprox  Error")
    while error > e:
        i = 0
        xk = g(x[k-1])
        x.append(xk)
        error = abs(x[k] - x[k-1])
        if i % 4 == 0 and i != 0:
            input("Enter to continue")
        print(k, "  ", round(xk, DD), "  ", round(error, DD))
        await_if_4(k)
        i += 1
        k += 1
    print("Number of iterations:", k)

fixed_point(g, x_0, h)
