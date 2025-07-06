def gauss_seidel(n):
    x = 0.0
    y = 0.0
    z = 0.0
    w = 0.0

    for i in range(1, n+1):
        x_new = 1 - 0.1 * y - 0.1 * z
        y_new = 2 - 0.1 * x_new - 0.1 * z
        z_new = 2 - 0.1 * x_new - 0.1 * y_new - 0.1 * w
        w_new = 1 - 0.1 * x_new - 0.1 * z_new

        x = x_new
        y = y_new
        z = z_new
        w = w_new

        print("Iter " + str(i) + ": x=" + str(round(x, 6)) + ", y=" + str(round(y, 6)) +
              ", z=" + str(round(z, 6)) + ", w=" + str(round(w, 6)))

    return x, y, z, w

gauss_seidel(8)
