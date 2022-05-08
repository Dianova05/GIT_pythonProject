# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# #1
# while True:
#     number_month = input("Введите месяц в виде целого числа от 1 до 12: >>> ")
#
#     if number_month.isdigit():
#         number_month = int(number_month)
#     else:
#         print('Ошибка ввода, это не число')
#         break
#
#     if number_month < 1 or number_month > 12:
#         print(f"Введен некоректный номер месяца")
#         break
#
#     season_list = [('Весна', 3, 4, 5), ('Лето', 6, 7, 8), ('Осень', 9, 10, 11), ('Зима', 12, 1, 2)]
#     for season in season_list:
#         for x in season:
#             if number_month == x:
#                 print(season[0])

# #2
# values
while True:
    number_month = input("Введите месяц в виде целого числа от 1 до 12: >>> ")

    if number_month.isdigit():
        number_month = int(number_month)
    else:
        print('Ошибка ввода, это не число')
        break

    if number_month < 1 or number_month > 12:
        print(f"Введен некоректный номер месяца")
        break

    season_dict = {"Зима": [1, 2, 12], "Весна": [3, 4, 5], "Лето": [6, 7, 8], "Осень": [9, 10, 11]}
    for key in season_dict.keys():
        for x in season_dict.get(key):
            if number_month == x:
                print(key)




