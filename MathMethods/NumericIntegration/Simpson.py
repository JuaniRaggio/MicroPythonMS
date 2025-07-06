import math

DD = 4
a = 1
b = 3
show_table = True
epsilon = 0.001
c_4 = 1.17

def f(x):
    return 1/(math.sqrt(1 + x**3))

def simpson_required_n(a, b, C_4, epsilon):
    numerador = (b - a)**5 * C_4
    denominador = 180 * epsilon
    n = ((numerador / denominador) ** 0.25)
    n = math.ceil(n)
    if n % 2 != 0:
        n += 1  # Simpson requiere n par
    return n

# n = simpson_required_n(a, b, c_4, epsilon)

def simpson_simple(f, a, b):
    m = (a + b) / 2
    return (b - a) * (f(a) + 4*f(m) + f(b)) / 6

def simpson_compuesto(f, a, b, n, show_table):
    if n % 2 != 0:
        raise ValueError("even n required")

    h = (b - a) / n
    suma = f(a) + f(b)
    print("i  xi  f(xi)  coef")
    for i in range(1, n):
        xi = a + i * h
        coef = 4 if i % 2 != 0 else 2
        suma += coef * f(xi)
        if show_table:
            print(i, "  ", round(xi, DD), "  ", round(f(xi), DD), "  ", coef)
    
    return (h / 3) * suma

print(simpson_compuesto(f, a, b, 4, show_table))
input("Enter to continue with next table")
print(simpson_compuesto(f, a, b, 8, show_table))
