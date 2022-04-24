# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

a = int(input("Введите результат пробежки 1 дня, в км: "))
b = int(input("Введите желаемый результат пробежки в км: "))
day = 1
while a <= b:
    delta = a * 0.1
    a = a + delta
    day = day + 1
print(f"на {day}-й день спортсмен достиг результата — не менее {b} км.")