#1. Создать программно файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

my_list = []
while True:
    line = input("Введите данные (об окончании ввода свидетельствует пустая строка): ")
    if line == '':
        print(my_list)
        exit()
    else:
        newline = line + '\n'
        my_list.append(newline)

    with open("test_01.txt", 'a+') as file_obj:
        file_obj.writelines(my_list)