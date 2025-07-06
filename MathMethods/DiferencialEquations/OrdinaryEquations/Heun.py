import math

def heun(f, a, b, y0, h):
    n = int((b - a) / h)
    t = a
    y = y0
    for _ in range(n):
        k1 = f(t, y)
        k2 = f(t + h, y + h * k1)
        y += (h / 2) * (k1 + k2)
        t += h
    return y

def f(t, y):
    return math.sin(t - y + 1)**2

# Paso h = 0.2
y_02 = heun(f, 0, 1, 0, 0.2)

# Paso h = 0.1
y_01 = heun(f, 0, 1, 0, 0.1)

# Extrapolación de Richardson
y_rich = (4 * y_01 - y_02) / 3

print("y(1) con h=0.2 =", y_02)
print("y(1) con h=0.1 =", y_01)
print("Extrapolación =", y_rich)
