import math

DD = 4
x0 = 0
y0 = 1
dy0 = None
stepSize_h = 0.2
n = 5

def f(X, Y):
    return (2 - 0.2 * Y) / 1.1

def y_real(x):
    return (x + 1)**2 - 0.5 * math.exp(x)

def euler_order_2(f, x0, y0, dy0, stepSize_h, n):
    x = [x0]
    y = [y0]
    dy = [dy0]

    print("x\ty_aprox\tdy_aprox")
    print(str(x0) + "\t" + str(y0) + "\t" + str(dy0))

    for _ in range(1, n + 1):
        xi = x[-1] + stepSize_h
        dyi = dy[-1] + stepSize_h * f(x[-1], y[-1], dy[-1])
        yi = y[-1] + stepSize_h * dy[-1]

        x.append(xi)
        y.append(yi)
        dy.append(dyi)

        print(str(round(xi, DD)) + "\t" + str(round(yi, DD)) + "\t" + str(round(dyi, DD)))
    # print(str(n) + "\t" + str(x[-1]) + "\t" + str(y[-1]) + "\t" + str(y_real(x[-1])) + "\t" + str(abs(y[-1] - y_real(x[-1]))))
    return x, y, dy

def euler(f, x0, y0, stepSize_h, n):
    x = [x0]
    y = [y0]
    print("x\taprox\terror")
    print(str(x0) + "\t" + str(y0) + "\t" + str(abs(y0 - y_real(x0))))
    for _ in range(1, n+1):
        xi = x[-1] + stepSize_h
        yi = y[-1] + stepSize_h * f(x[-1], y[-1])
        x.append(xi)
        y.append(yi)
        err = round(abs(yi - y_real(xi)), DD)
        print(str(round(xi, DD)) + "\t" + str(round(yi, DD)) + "\t" + str(round(err, DD)))
    # print(str(round(x[-1], DD)) + "\t" + str(round(y[-1], DD)) + "\t" + "\t" + str(round(abs(y[-1] - y_real(x[-1])), DD)))
    return x, y

euler(f, x0, y0, stepSize_h, n)
# euler_order_2(f, x0, y0, dy0, stepSize_h, n)

