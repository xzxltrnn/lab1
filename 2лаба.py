#Задание 1.1:
def greet(name, msg):
    print("Привет,", name + '. ' + msg)
greet('Дима', 'Доброе утро!' )


#Задание 1.2:
def square(num):
    return num ** 2
res = square(75)
print(res)

#Задание 1.3:
def max_of_two(num1, num2):
    return num1 if num1 > num2 else num2
res = max_of_two(32, 43)
print(res)

#Задание 2:
def describe_person(name, age=30):
    print(f"Имя: {name}, Возраст: {age}")

describe_person("Антон")
describe_person("Дарья", 25)

#Задание 3:
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


print(is_prime(11))
print(is_prime(4))
print(is_prime(17))


