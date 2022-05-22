# This Python file uses the following encoding: utf-8
# 4.Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    __speed = 0
    __direction = None

    def __init__(self, speed, color, name, is_police):
        self.__speed = speed
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'Автомобиль {self.name} поехал'

    def stop(self):
        return f'Автомобиль {self.name} остановился'

    def turn_right(self):
        return f'Автомобиль {self.name} повернул вправо'

    def turn_left(self):
        return f'Автомобиль {self.name} повернул влево'

    def show_speed(self):
        return f'Текущая скорость автомобиля {self.name} {self.speed} км/ч'


class TownCar(Car):
    MAX_SPEED = 60

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > self.MAX_SPEED:
            print(f'Превышение скорости автомобилем {self.name}!')
        print(f'Текущая скорость автомобиля {self.name}: {self.speed}км/ч')


class SportCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class WorkCar(Car):
    MAX_SPEED = 40

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > self.MAX_SPEED:
            print(f'Превышение скорости автомобилем {self.name}!')
        print(f'Текущая скорость автомобиля {self.name}: {self.speed}км/ч')


class PoliceCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


if __name__ == '__main__':
    pc = PoliceCar(180, 'голубой', 'Ниссан')
    wc1 = WorkCar(12, 'зеленый', 'Скания')
    wc2 = WorkCar(120, 'оранжевый', 'КАМАЗ')
    sc = SportCar(200, 'красный', 'АУДИ')
    tc1 = TownCar(80, 'серый', 'Вольво')
    tc2 = TownCar(60, 'черный', 'БМВ')
    pc.show_speed()
    pc.go()
    pc.show_speed()
    pc.stop()
    print(pc.color)
    pc.go()
    print(pc.name)
    wc1.go()
    wc2.go()
    sc.go()
    tc1.go()
    tc2.go()
    wc1.show_speed()
    wc2.show_speed()
    sc.show_speed()
    tc1.show_speed()
    tc2.show_speed()
    print(pc.turn_right())
    print(wc1.stop())
    print(wc1.go())
    print(tc1.turn_right())
    print(tc2.show_speed())
    print(sc.turn_left())
