# Modify this parameters to your preference
L_x = 1
R_x = L_x + 1
eTolerance = 0.001

def f(x):
    return x**3 + 2 * x ** 2 -5 * x - 4

def look_for_interval_for_bolzano(f, cte=1, start=-10, end=10):
    for a in range(start, end):
        if verify_bolzano(f, cte, cte + 1):
            print("The interval: (", a, ", ", a + cte, ") verifies bolzano")

def verify_bolzano(f, a, b):
    return f(a) * f(b) > 0

def biseccion(f, a, b, eTolerance):

    if verify_bolzano(f, a, b):
        print("Doesn't verify Bolzano")
        return None

    error = b - a
    k = 0

    c_aprox = []
    while error > eTolerance:
        c = (a + b)/2
        c_aprox.append(c)

        if f(a)*f(c) < 0:
            b = c
        else:
            a = c

        error = (b-a)/2

        k += 1

        # print("x value for root (c):", c, "; Error:", error)
    print("x root (c) in last step:", c_aprox[-1])
    print("Number of iterations: ", k, ", this means ", k + 1, " steps")

biseccion(f, L_x, R_x, eTolerance)
