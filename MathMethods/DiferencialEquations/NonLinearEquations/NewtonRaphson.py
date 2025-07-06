# Modify this parameters and function for you specific case
x_0 = 0
eTolerance = 0.0001

def f(x):
    return None

def f_prime(x):
    return None

def newton(f, f_prime, x0, e):
    x = [x0]
    error = 1
    k = 0

    while error > e:
        if f_prime(x[k]) == 0:
            print("Derivada nula. No se puede continuar.")
            return None

        xk = x[k] - f(x[k]) / f_prime(x[k])
        x.append(xk)

        error = abs(xk - x[k])

        print(xk, error)
        k += 1

    print("Number of iterations:", k)
    return x[-1]

newton(f, f_prime, x_0, eTolerance)
