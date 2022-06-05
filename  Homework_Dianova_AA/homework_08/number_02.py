# This Python file uses the following encoding: utf-8
# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.

class DivisionByZero(Exception):
    def __init__(self, txt):
        self.txt = txt


def my_division():
    try:
        divider = int(input("Введите делимое: "))
        denominator = int(input("Введите делитель: "))
        if denominator == 0:
            raise DivisionByZero("Ошибка: Происходит деление на 0. Деление на 0 невозможно!")
        else:
            total = divider / denominator
            return f"Результат деления: {divider} / {denominator} = {total}"
    except ValueError:
        return "Неправильный ввод. Введите число"
    except DivisionByZero as my_error:
        return my_error


print(my_division())