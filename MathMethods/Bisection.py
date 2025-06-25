def biseccion(f,a,b,e):

    error = b - a
    k = 0

    c_aprox = []
    while error > e:
        c = (a + b)/2
        c_aprox.append(c)

        if f(a)*f(c) < 0:
            b = c
        else:
            a = c

        error = (b-a)/2

        k += 1

        print(c, error)
    print("Number of iterations: ", k)



def f(x):
    return x**3 + x - 4

biseccion(f, 1, 20, 0.001)
