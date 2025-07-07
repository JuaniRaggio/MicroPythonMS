X = [-2, 0, 2, 3]
Y = [0, -1, 0, 0]

x_eval = 2

def lagrange_coefficients(x_vals, x_eval):
    n = len(x_vals)
    L = []
    for i in range(n):
        numerador = 1.0
        denominador = 1.0
        for j in range(n):
            if i != j:
                numerador *= (x_eval - x_vals[j])
                denominador *= (x_vals[i] - x_vals[j])
        L.append(numerador / denominador)
    return L

def delta_poly(i, X, x):
    p = 1
    for x_k in X:
        if x_k != X[i]:
            p *= (x - x_k) / (X[i] - x_k)
    return p

def lagrange_poly(X, Y, x):
    if X.len() != Y.len():
        return None
    L = 0
    for i in range(len(Y)):
        L += Y[i] * delta_poly(i, X, x)
    return L

print("Lagrange coefficients: ", lagrange_coefficients(X, x_eval))
print("P(", x_eval, ") =", lagrange_poly(X, Y, x_eval))
