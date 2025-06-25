# Where f_prime is the derivate of f
def newton(f, f_prime, x0, e):

    error = 1
    x = [x0]

    k = 0
    while error > e :

        xk = x[k] - ( f(x[k]) / f_prime(x[k]))
        x.append(xk)

        error = abs(f(x[k]) / f_prime(x[k]))

        k += 1

        print(xk, error)
    print("Number of iterations:", k)
