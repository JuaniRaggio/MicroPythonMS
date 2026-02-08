iterations = 8

A = [
    [1, 0.1, 0.1, 0],
    [0.1, 1, 0.1, 0],
    [0.1, 0.1, 1, 0.1],
    [0.1, 0, 0.1, 1]
]

b = [1, 2, 2, 1]

def jacobi_general(A, b, iterations):
    n = len(A)
    x_old = [0.0] * n
    x_new = [0.0] * n

    for it in range(1, iterations + 1):
        for i in range(n):
            suma = sum(A[i][j] * x_old[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - suma) / A[i][i]

        print("Iter", it, ":", ", ".join(["x" + str(i+1) + "=" + str(round(val, 6)) for i, val in enumerate(x_new)]))

        # copiar los nuevos valores como los actuales para la siguiente iteración
        x_old = x_new.copy()

        if it % 4 == 0:
            input("Enter to continue")

    return x_new

jacobi_general(A, b, iterations)
