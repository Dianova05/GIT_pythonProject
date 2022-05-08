#1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def my_div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Делить на ноль нельзя")

a, b = map(int, input("Введите числа: ").split())
print(my_div(a, b))