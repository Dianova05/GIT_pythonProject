# This Python file uses the following encoding: utf-8
# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список только числами.
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта,
# введя, например, команду “stop”. При этом скрипт завершается, сформированный список с числами выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. При вводе пользователем
# очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число.
# Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
# При этом работа скрипта не должна завершаться.

class StrException(Exception):
    pass


total_list = []

while True:
    in_list = input("Введите число или 'stop' для завершения скрипта: ")
    if in_list == 'stop':
        print(f"Список: {total_list}")
        break
    try:
        if not in_list.isdigit():
            raise StrException(f"Вы ввели: '{in_list}' \t Пожалуйста, введите число: ")
    except StrException as error:
        print(error)

    else:
        total_list.append(in_list)