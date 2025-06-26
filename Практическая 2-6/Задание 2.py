class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password
    def __str__(self):
        return f"login: {self.login}, Пароль: {self.password}"
users = [
    User('admin', 'qwe123'),
    User('steil', '123qwe'),
    User('Max', '123456789'),
    User('schole', 'asdasf'),
    User('Kent', 'Parol')
]
def search(login, password, user_list):
    for i in user_list:
        if i.login == login and i.password == password:
            return i
        return None
search_login = 'admin'
search_password = 'qwe123'
search_user = search(search_login, search_password, users)
if search_user:
    print(f"Пользователь найден, {search_user}")
else:
    print("Ненайден пользователь")