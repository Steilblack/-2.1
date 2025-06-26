d = lambda x, y : x ** 2 + y ** 2
x, y, r = map(float, input("Введите числа через пробел: ").split())
print(f"Точка {x}, {y} принадлежит кругу с радиусом {r}" if d(x, y) <= r ** 2 else "Не принадлежит")