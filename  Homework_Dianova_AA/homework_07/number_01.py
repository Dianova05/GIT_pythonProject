# This Python file uses the following encoding: utf-8
# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: см. в методичке.
#
# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
# первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        for row in self.my_list:
            for i in row:
                print(f"{i:3}", end=" ")
            print()
        return " "

    def __add__(self, other):
        for a in range(len(self.my_list)):
            for b in range(len(other.my_list[a])):
                self.my_list[a][b] = self.my_list[a][b] + other.my_list[a][b]
        return Matrix.__str__(self)


matrix = Matrix(
    [
        [4, 16, 11],
        [20, 14, 5],
        [9, 7, -4]
    ]
)
my_matrix = Matrix(
    [
        [3, 4, 4],
        [30, 16, 15],
        [21, -2, -6]
    ]
)

print(matrix.__add__(my_matrix))