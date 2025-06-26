class Fitnes_center:
    def __init__(self, code, year, month, time):
        self.code = code
        self.year = year
        self.month = month
        self.time = time
    def __str__(self):
        return f"Клиент: {self.code}, Дата: {self.year}. {self.month}, Длительность: {self.time} минут"
sesiya = [
    Fitnes_center("A1", 2023, 1, 60),
    Fitnes_center("A2", 2023, 2, 120),
    Fitnes_center("A3", 2023, 2, 45),
    Fitnes_center("A4", 2024, 3, 60),
    Fitnes_center("A5", 2024, 3, 90),
    Fitnes_center("A6", 2024, 4, 60),
    Fitnes_center("A7", 2025, 4, 45),
    Fitnes_center("A8", 2025, 5, 120),
    Fitnes_center("A9", 2025, 6, 180),
    Fitnes_center("A10", 2025, 6, 135)
]
long_lesson = {}
for i in sesiya:
    if i.year in long_lesson:
        long_lesson[i.year] += i.time
    else:
        long_lesson[i.year] = i.time
max_time_lesson = max(long_lesson.values())
max_year = [year for year, time in long_lesson.items() if time == max_time_lesson]
rezult = min(max_year) if max_year else None
if rezult is not None:
    print(f"Год с наибольшей суммарной продолжительностью: {rezult}")
    print(f"Суммарная продолжительность: {max_time_lesson} минут")
else:
    print("Нет данных для анализа")
