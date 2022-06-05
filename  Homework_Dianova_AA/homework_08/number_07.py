# This Python file uses the following encoding: utf-8
# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку методов
# сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив
# сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class Complexus:

    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __add__(self, other):
        return Complexus((self.re + other.re), (self.im + other.im))

    def __mul__(self, other):
        return Complexus((self.re * other.re - (self.im * other.im)), (self.re * other.im + self.im * other.re))

    def __str__(self):
        return f'Input Compnumber >>> {self.re} + {self.im}i'


num_1 = Complexus(3, 2)
num_2 = Complexus(2, -3)
print(num_1)
print(num_2)
print(f"Операция сложения комплексных чисел:  {num_1 + num_2}")
print(f"Операция умножения компексных чисел: {num_1 * num_2}")


