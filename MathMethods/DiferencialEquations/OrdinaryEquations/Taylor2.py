a = None
b = None
y0 = None
h = None
interval = [a, b]

def f(x, y):
    return NotImplemented

def f_prime(x, y):
    return NotImplemented

def taylor2(interval, F, F_prime, y_0, h):
    partitions = int((interval[1] - interval[0]) / h)
    y = [0] * (partitions+1)
    y[0] = y_0
    h = (interval[1] - interval[0]) / partitions
    for i in range(0, partitions):
        t = i * h + interval[0]
        y[i+1] = y[i] + F(t, y[i]) * h + F_prime(t, y[i]) * h * h / 2
    return y

print(taylor2(interval, f, f_prime, y0, h))
