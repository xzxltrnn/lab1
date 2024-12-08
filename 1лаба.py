my_list =[1,2,3,4,5,6,7,8,9,10]

print(my_list[0])
print(my_list[2])
print(my_list[-1])

my_list[1] = 100

for i in range(1, 11):
    print(i)

i = 10
while i >=1:
    print(i)
    i -=1

num = int(input("Введите число: "))
if num > 0:
    print("Число положительное")
elif num < 0:
    print ("Число отрицательное")
else:
    print("Число равно нулю")

num = int(input("Введите число: "))
for i in range(1, num + 1):
    print(i)

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
if num1 > num2:
    print("Большее число: ", num1)
else:
    print("Большее число: ", num2)
