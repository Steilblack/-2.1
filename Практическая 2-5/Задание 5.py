def equation(a,b):
    suma = (a + b * 4) * (a - 3 * b) + a ** 2
    return suma
a = int(input("Число а: "))
b = int(input("Число b: "))
print(equation(a, b))
