lis = ["Маша", "Кирилл", "Вова", "Ольга", "Алиса", "Иван", "Артем", "Александр", "Валера", "Настя"]
arr = list(filter(lambda name: name.startswith("А"), lis))
print(arr)