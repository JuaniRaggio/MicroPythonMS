X = [1, 2, 3]
Y = [1, 4, 9]

def newton_coeff(X, Y):
    M = []
    M.append(Y)
    n = len(Y)
    for i in range(n-1):
        last = M[i]
        next = []
        for k in range(n-i-1):
            next.append((last[k+1] - last[k]) / (X[k+i+1] - X[k]))
        M.append(next)
    return [M[i][0] for i in range(n)]

def newton_poly(X, Y, x):
    coeff = newton_coeff(X, Y)
    n = len(coeff)-1
    q = coeff[n]
    for i in range(n):
        q = coeff[n-i-1] + q*(x-X[n-i-1])
    return q

print(newton_poly(X, Y, 2.5))
