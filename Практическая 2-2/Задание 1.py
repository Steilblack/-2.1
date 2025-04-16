class Student:
    def __init__(self, lastname, birthday, number_group,grade):
        self.lastname = lastname
        self.birthday = birthday
        self.number_group = number_group
        self.grade = grade
    def change_lastname(self, new_lastname):
        self.lastname = new_lastname
    def change_birthday(self, new_birthday):
        self.birthday = new_birthday
    def change_number_group(self, new_number_group):
        self.number_group = new_number_group
    def change_grade(self, new_grade):
        self.grade = new_grade
    def get_information(self):
        print(f"Фамилия: {self.lastname}")
        print(f"Дата рождения: {self.birthday}")
        print(f"Номер группы: {self.number_group}")
        print(f"Успеваемость: {self.grade}")
def search():
    user_lastname = input("Введите фамилию студента для поиска: ")
    user_birthaday = input("Введите дату рождения для поиска: ")
    search = None
    for i in students:
        if i.lastname == user_lastname and i.birthday == user_birthaday:
            search = i
            break
    if search:
        print("Студент найден: ")
        search.get_information()
    else:
        print("Студент не найден")
def new_student():
    lastname = input("Введите фамилию: ")
    birthday = input("Введите дату рождения")
    number_group = input("Введите номер группы")
    grade_str = input("Введите оценки через запятые")
    grade = [int(x) for x in grade_str.split(',')]
    return Student(lastname, birthday, number_group, grade)
def information_all_stutent():
    for i in students:
        i.get_information()
students = []
user_student = new_student()
students.append(user_student)
student1 = Student("Заблоцкий", "13.01.1995", 643, [5,4,4,5,2])
students.append(student1)
student1.change_lastname("Попов")
student1.change_birthday("26.04.1995")
student1.change_number_group(731)
student1.change_grade([5,2,3,5,5])
information_all_stutent()
search()