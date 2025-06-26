class Fitnes_center:
    def __init__(self, code, year, month, time):
        self.code = code
        self.year = year
        self.month = month
        self.time = time
    def __str__(self):
        return f"Клиент: {self.code}, Дата: {self.year}. {self.month}, Длительность: {self.time} минут"
sesiya = [
    Fitnes_center("A1", 2025, 1, 60),
    Fitnes_center("A2", 2025, 2, 120),
    Fitnes_center("A3", 2025, 2, 45),
    Fitnes_center("A4", 2025, 3, 60),
    Fitnes_center("A4", 2025, 3, 90)
]
long_lesson = max(sesiya, key=lambda x: x.time)
short_lesson = min(sesiya, key=lambda x: x.time)
print(long_lesson)
print(short_lesson)