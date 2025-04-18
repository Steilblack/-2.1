class Worker:
    def __init__(self, name, surname, rate, days,):
        self.__name = name
        self.__surname = surname
        self.__rate = rate
        self.__days = days
    @property
    def get_name(self):
        return self.__name
    @property
    def get_surname(self):
        return self.__surname
    @property
    def get_rate(self):
        return self.__rate
    @property
    def get_days(self):
        return self.__days
    @property
    def GetSalary(self):
        self.salary = self.__rate * self.__days
        return self.salary
    def information_worker(self):
        print(f"Имя: {self.__name}")
        print(f"Фамилия: {self.__surname}")
        print(f"Ставка за день: {self.__rate}")
        print(f"Количество отработаных дней: {self.__days}")
        print(f"Зарплата: {self.salary}")
worker1 = Worker("Владимир", "Заблоцкий", 500, 30)
print(worker1.get_name)
print(worker1.get_surname)
print(worker1.get_rate)
print(worker1.get_days)
print(worker1.GetSalary)