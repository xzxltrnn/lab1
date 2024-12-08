class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def set_password(self, new_password):
        self.password = new_password

    def check_password(self, password):
        return self.password == password

    def get_username(self):
        return self.username

user = UserAccount('Богдан', 'богдан@example.com', '1234')

print(user.check_password('1234'))

user.set_password('new_1234')

print(user.check_password('new_1234'))
print(user.check_password('wrong_password'))




class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        return f"Марка: {self.make}, Модель: {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Тип топлива: {self.fuel_type}"


car = Car('LADA','Vesta', 'Бензин')
print(car.get_info())
