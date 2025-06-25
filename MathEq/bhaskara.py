import math

def bhaskara(a:float, b:float, c:float):
    disc = math.pow(b, 2) - 4*a*c
    img = False
    if disc < 0:
        disc *= -1
        return f"x in C -> [x, yi] = {[-b/(2*a), math.sqrt(disc)/(2*a)]}"
    real1 = (-b + math.sqrt(disc))/(2*a)
    real2 = (-b - math.sqrt(disc))/(2*a)
    return f"x_1(+): {real1}; x_2(-): {real2}"

a = float(input("A: "))
b = float(input("B: "))
c = float(input("C: "))
print(bhaskara(a, b, c))

