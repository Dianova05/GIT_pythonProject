#1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
import sys
name_file, time_work, salary, bonus = sys.argv
try:
    time_work = float(time_work)
    salary = float(salary)
    bonus = float(bonus)
    res = (time_work * salary) + bonus
    print(f'заработная плата для сотрудника = {res} руб.')
except ValueError:
    print('Введено не число!')