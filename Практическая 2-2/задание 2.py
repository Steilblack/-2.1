class Train:
    def __init__(self,name_destination, number_train, departure_time):
        self.name_destination = name_destination
        self.number_train = number_train
        self.departure_time = departure_time
    def information_train(self):
        print(f"Пункт назначения: {self.name_destination}")
        print(f"Номер поезда: {self.number_train}")
        print(f"Время отправления: {self.departure_time}")
def serch():
    user_number_train = input("Введите номер поезда: ")
    try:
        user_number_train = int(user_number_train)
    except ValueError:
        print("ОШИБКА! Введите нормальный номер поезда (число)")
        return
    serch = None
    for i in train:
        if i.number_train == user_number_train:
            serch = i
            break
    if serch:
        print("Информация о поезде: ")
        serch.information_train()
    else:
        print("Поезд не найден")
train = []
train1 = Train("Москва", 11, "01.06.2025-13:00")
train.append(train1)
train1.information_train()
serch()