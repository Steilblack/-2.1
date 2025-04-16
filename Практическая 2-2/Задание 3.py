class Num_int:
    def __init__(self, num1, num2):
        if not isinstance(num1, int) or not isinstance(num2, int):
            raise TypeError("Оба згачения должны быть целыми числами")
        self.num1 = num1
        self.num2 = num2
    def screen_output(self):
        print(f"Первое число: {self.num1}")
        print(f"Второе число: {self.num2}")
    def change_num(self, new_num1, new_num2):
        self.num1 = new_num1
        self.num2 = new_num2
        print("Числа изменены")
    def summa_num(self):
        return self.num1 + self.num2
    def largest_num(self):
        return max(self.num1, self.num2)
num = Num_int(10, 5)
num.change_num(3, 7)
num.screen_output()
suma = num.summa_num()
print(f"Сумма: {suma}")
largest = num.largest_num()
print(f"Наибольшее: {largest}")