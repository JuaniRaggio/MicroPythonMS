import math

steps = 1
step_size = 0.23
y_0 = 1
a = -1
b = 1
interval = [a, b]

def f(t, y):
    return y

def runge_kutta_order2(interval, F, y_0, step_size, coef):
    partitions = int((interval[1] - interval[0]) / step_size)
    (a, b, p, q) = coef
    y = [0] * (partitions+1)
    y[0] = y_0
    step_size = (interval[1] - interval[0]) / partitions
    for i in range(0, partitions):
        t = i * step_size + interval[0]
        k1 = F(t, y[i]) * step_size
        k2 = F(t + p*step_size, y[i] + q*k1) * step_size
        y[i+1] = y[i] + a*k1 + b*k2
    return y

def runge_kutta_order3(f, y0, step_size, steps):
    ys = []
    t = 0
    y = y0
    for _ in range(steps):
        k1 = step_size * f(t, y)
        k2 = step_size * f(t + step_size / 2, y + k1 / 2)
        k3 = step_size * f(t + step_size, y - k1 + 2 * k2)
        y = y + (k1 + 4 * k2 + k3) / 6
        t = t + step_size
        ys.append((t, y))
    return ys

def runge_kutta_forth_order(interval, F, y_0, step_size):
    partitions = int((interval[1] - interval[0]) / step_size)
    y = [0] * (partitions+1)
    y[0] = y_0
    step_size = (interval[1] - interval[0]) / partitions
    for i in range(partitions):
        t = i * step_size + interval[0]
        k1 = F(t, y[i]) * step_size
        k2 = F(t + step_size/2, y[i] + k1/2) * step_size
        k3 = F(t + step_size/2, y[i] + k2/2) * step_size
        k4 = F(t + step_size, y[i] + k3) * step_size
        y[i+1] = y[i] + (k1 + 2*k2 + 2*k3 + k4)/6
    return y

print(runge_kutta_order3(f, y_0, step_size, steps))

