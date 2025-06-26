class Task:
    def __init__(self, datestart, datefinish, description):
        self.datestart = datestart
        self.datefinish = datefinish
        self.description = description
    def __str__(self):
        return f'Начало:{self.datestart} Конец:{self.datefinish} Описание:{self.description}'
tasks = [
    Task("01-07-2025 08:00", "01-07-2025 08:30", "Поездка на место"),
    Task("01-07-2025 08:30", "01-07-2025 09:00", "Подготовка к приему"),
    Task("01-07-2025 09:00", "01-07-2025 16:00", "Закупка дикоросов"),
    Task("01-07-2025 16:00", "01-07-2025 17:00", "Возвращение на базу"),
    Task("01-07-2025 17:00", "01-07-2025 22:00", "Переработка закупленого")
]
last_task = max(tasks, key=lambda task: task.datefinish)
print(last_task)