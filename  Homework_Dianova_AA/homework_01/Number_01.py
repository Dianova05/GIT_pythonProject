# 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько
# чисел и строк и сохраните в переменные, выведите на экран.

    # Вариант 1
value = 2 + 3
print(value)

    # Вариант 2
a = int(input("Введите целое число: "))
b = 5
print(a + b)

    # Вариант 3
names = input("Введите Ваше имя: ")
surnames = input("Введите Вашe фамилию: ")
print(f"Ф.И.: {surnames} {names}")

    # Вариант 4
names = input("Введите Ваше имя: ")
age = int(input("Введите Ваш возраст: "))
if age < 18:
    print(f"{names} Вам нет 18 лет! Несоответствие возрастному ограничению.")
else:
    print(f"{names}, добро пожаловать на наш сайт знакомств!")