import math
import datetime
number = float(input("Введите число для вычисления квадратного корня: "))
square_root = math.sqrt(number)
print(f"Квадратный корень числа {number}: {square_root}")
current_datetime = datetime.datetime.now()
print("Текущая дата и время:", current_datetime)






import my_module
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
result = my_module.add_numbers(num1, num2)
print(f"Сумма {num1} и {num2} равна {result}.")

