import math

# Modify this functions to you preference

# y_real is to compare the real value vs your aproximation
def y_real(x):
    return (x + 1)**2 - 0.5 * math.exp(x)

def f(t, y, z):
    return -0.1 * z + 0.9 * y + 1 / (1 + t)

def euler_order_2(f, x0, y0, dy0, stepSize_h, n):
    x = [x0]
    y = [y0]
    dy = [dy0]

    print("i\tx\t\ty_aprox\t\tdy_aprox")
    print("0\t" + str(x0) + "\t" + str(y0) + "\t" + str(dy0))

    for i in range(1, n + 1):
        xi = x[-1] + stepSize_h
        dyi = dy[-1] + stepSize_h * f(x[-1], y[-1], dy[-1])
        yi = y[-1] + stepSize_h * dy[-1]

        x.append(xi)
        y.append(yi)
        dy.append(dyi)

        # print(str(i) + "\t" + str(xi) + "\t" + str(yi) + "\t" + str(dyi))
    print(str(n) + "\t" + str(x[-1]) + "\t" + str(y[-1]) + "\t" + str(y_real(x[-1])) + "\t" + str(abs(y[-1] - y_real(x[-1]))))
    return x, y, dy

def euler(f, x0, y0, stepSize_h, n):
    x = [x0]
    y = [y0]
    print("i\tx\t\ty_aprox\t\ty_real\t\terror")
    print("0\t" + str(x0) + "\t" + str(y0) + "\t" + str(y_real(x0)) + "\t" + str(abs(y0 - y_real(x0))))
    for i in range(1, n+1):
        xi = x[-1] + stepSize_h
        yi = y[-1] + stepSize_h * f(x[-1], y[-1])
        x.append(xi)
        y.append(yi)
        # err = abs(yi - y_real(xi))
        # print(str(i) + "\t" + str(xi) + "\t" + str(yi) + "\t" + str(y_real(xi)) + "\t" + str(err))
    print(str(n) + "\t" + str(x[-1]) + "\t" + str(y[-1]) + "\t" + str(y_real(x[-1])) + "\t" + str(abs(y[-1] - y_real(x[-1]))))
    return x, y


euler_order_2(f, x0=0, y0=1, dy0=1, stepSize_h=0.1, n=10)
