from my_package import add, subtract, concatenate, repeat_string

num1 = 10
num2 = 5
result_add = add(num1, num2)
result_subtract = subtract(num1, num2)

print(f"Сумма {num1} и {num2} равна {result_add}.")
print(f"Разность {num1} и {num2} равна {result_subtract}.")

str1 = "Hello"
str2 = " World"
result_concat = concatenate(str1, str2)
result_repeat = repeat_string(str1, 3)

print(f"Объединенная строка: {result_concat}.")
print(f"Повторенная строка: {result_repeat}.")
