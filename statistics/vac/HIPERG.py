# N: Population size
N = int(input("Population size: "))

# K: Amount of successes in population
K = int(input("Successes in population: "))

# n: Extraction size
n = int(input("Extraction size: "))

# x: Amount of successes in extraction
x = int(input("Successes in extraction: "))

# mu_X = E[X] = n K/N
# sigma_X^2 = V[X] = mu_X (1 - K/N) (N - n)/(N - 1)

def fact(num):
    res = 1
    while num > 0:
        res *= num
        num -= 1
    return res

def comb(a, b):
    if a < b or a < 0 or b < 0:
        return 0
    numerator = fact(a)
    denominator = fact(b) * fact(a - b)
    return numerator//denominator

K_x = comb(K, x)
NK_nx = comb(N - K, n - x)
Nn = comb(N, n)

def hiperpdf():
    return (K_x * NK_nx)/Nn

def hipercdf():
    res = 0
    i = 0
    while i <= x:
        res += comb(K, i) * comb(N - K, n - i)
        i += 1
    return res/Nn

print("pdf: ", hiperpdf())
print("cdf: ", hipercdf())
