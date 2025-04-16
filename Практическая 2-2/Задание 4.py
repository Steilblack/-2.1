class Count:
    def __init__(self, count = 0):
        self.count = count
    def increase(self):
        self.count += 1
        return self.count
    def decrease(self):
        self.count -= 1
        return self.count
    def current_status(self):
        return self.count
start_str = input("Введите начало счетчика")
if start_str:
    start_value = int(start_str)
else:
    start_value = 0
counter = Count(start_value)
print(f"Начальное значение: {counter.current_status()}")
print(f"Увеличиваем: {counter.increase()}")
print(f"Уменьшаем: {counter.decrease()}")
print(f"Текущее значение: {counter.current_status()}")