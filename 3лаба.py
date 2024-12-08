#
acb = ()

with open('example.txt', 'w', encoding='utf-8') as file:
    file.write("1111\n")
    file.write("222fjfgj346\n")
    file.write("33679987033\n")

print("Файл example.txt создан и заполнен.")

#
def read_file(file_path, mode='all'):

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            if mode == 'all':
                content = file.read()
                print(content)
            elif mode == 'line':
                for line in file:
                    print(line, end='')
            else:
                print("Некорректный режим чтения. Используйте 'all' или 'line'.")
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
#
if acb == "Чтение всего файла сразу":
    print("\nЧтение всего файла сразу:")

read_file('example.txt', 'all')


print("\nПострочное чтение файла:")
read_file('example.txt', 'line')


def write_to_file(file_path, text, mode='w'):
    with open(file_path, mode, encoding='utf-8') as file:
        file.write(text + '\n')

#
user_text = input("Введите текст для записи в файл: ")
write_to_file('user_input.txt', user_text, 'w')
additional_text = input("Введите дополнительный текст для добавления в файл: ")
write_to_file('user_input.txt', additional_text, 'a')
print("Текст успешно записан в файл.")

#
def read_file(file_path, mode='all'):

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            if mode == 'all':
                content = file.read()
                print(content)
            elif mode == 'line':
                for line in file:
                    print(line, end='')
            else:
                print("Некорректный режим чтения. Используйте 'all' или 'line'.")
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")

print("\nЧтение всего файла сразу:")
read_file('example.txt', 'all')


