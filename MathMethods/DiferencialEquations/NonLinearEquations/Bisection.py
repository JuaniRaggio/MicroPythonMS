# Primero verificar que intervalo verifica bolzano
# luego asignarlo a L_x y R_x y descomentar la ultima
# linea
DD = 5
L_x = 1
R_x = L_x + 1
cte = 1
eTolerance = 0.001

def f(x):
    return x**3 + 2 * x ** 2 -5 * x - 4

def look_interval_for_bolzano(f, cte, start, end):
    for a in range(start, end):
        if verify_bolzano(f, cte, cte + 1):
            print("The interval: (", a, ", ", a + cte, ") verifies bolzano")

look_interval_for_bolzano(f, cte, L_x, R_x)

def await_if_4(n):
    if n % 4 == 0 and n != 0:
        input("Enter to continue")

def verify_bolzano(f, a, b):
    return f(a) * f(b) < 0

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

        print("On step", k, "x value for root (c):", round(c, DD), "; Error:", round(error, DD))
        k += 1

    print("x root (c) in last step:", round(c_aprox[-1], DD))
    print("Number of iterations: ", k, ", this means ", k + 1, " steps")

# biseccion(f, L_x, R_x, eTolerance)
