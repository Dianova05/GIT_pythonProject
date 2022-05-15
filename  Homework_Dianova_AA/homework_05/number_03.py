# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
#
# Иванов 23543.12
# Петров 13749.32

firm = {'Петров': 25000, 'Иванов': 24000, 'Сидоров': 15400, 'Зайцев': 24100, 'Волков': 23600, 'Крюков': 24200, 'Ли': 24300, 'Пушкин': 22000, 'Елисеев': 21000, 'Козлов': 19000}
try:
    file_obj = open("test_03.txt", 'w')
    for last_name, salary in firm.items():
        file_obj.write(last_name + ':' + str(salary) + "\n")
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    file_obj.close()
sal = []
persons = []
with open("test_03.txt", "r") as file_obj:
    for i in file_obj:
        i = i.split(':')
        if int(i[1]) < 20000:
            persons.append(i[0])
            sal.append(i[1])
print(f'Оклад меньше 20.000 {persons}, средний оклад {sum(map(int, sal)) / len(sal)}')