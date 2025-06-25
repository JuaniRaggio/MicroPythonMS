import math

def y_real(x):
    return (x + 1)**2 - 0.5 * math.exp(x)

def euler(f, x0, y0, h, n):
    x = [x0]
    y = [y0]
    print("i\tx\t\ty_aprox\t\ty_real\t\terror")
    print("0\t" + str(x0) + "\t" + str(y0) + "\t" + str(y_real(x0)) + "\t" + str(abs(y0 - y_real(x0))))
    for i in range(1, n+1):
        xi = x[-1] + h
        yi = y[-1] + h * f(x[-1], y[-1])
        x.append(xi)
        y.append(yi)
        err = abs(yi - y_real(xi))
        print(str(i) + "\t" + str(xi) + "\t" + str(yi) + "\t" + str(y_real(xi)) + "\t" + str(err))
    return x, y

# dy/dx = f(x, y) = y - x^2 + 1
def f(x, y):
    return y - x**2 + 1

euler(f, x0=0, y0=0.5, h=0.2, n=10)
