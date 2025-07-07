a = None
b = None
n = None
def f(x):
    return None

def simple_trapeze(f, a, b):
    return (b - a) * (f(a) + f(b)) / 2

def comp_trapeze(f, a, b, n):
    h = (b - a) / n
    suma = f(a) + f(b)
    for i in range(1, n):
        suma += 2 * f(a + i * h)
    return (h / 2) * suma

# print(simple_trapeze(f, a, b))
print(comp_trapeze(f, a, b, n))
