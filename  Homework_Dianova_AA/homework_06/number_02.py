# This Python file uses the following encoding: utf-8
# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного
# полотна. Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна. Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т

class Road:
    _length: float
    _width: float

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight_asphalt(self):
        weight_asphalt = 25
        dist_asphalt = 5
        print(f'Требуемая масса асфальта {(self._length * self._width * weight_asphalt * dist_asphalt) // 1000} т')


calc_example = Road(5000, 20)
calc_example.weight_asphalt()
