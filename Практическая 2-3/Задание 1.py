class Worker:
    def __init__(self, name, surname, rate, days,):
        self.name = name
        self.surname = surname
        self.rate = rate
        self.days = days
    def GetSalary(self):
        self.salary = self.rate * self.days
        return self.salary
    def information_worker(self):
        print(f"Имя: {self.name}")
        print(f"Фамилия: {self.surname}")
        print(f"Ставка за день: {self.rate}")
        print(f"Количество отработаных дней: {self.days}")
        print(f"Зарплата: {self.salary}")
worker1 = Worker("Владимир", "Заблоцкий", 500, 30)
print(f"Зарплата: {worker1.GetSalary()} рублей")
worker1.information_worker()