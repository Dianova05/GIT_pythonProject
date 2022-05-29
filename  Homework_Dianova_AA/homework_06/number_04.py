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
        self.speed = self.__speed

    def stop(self):
        self.speed = 0

    def turn(self, direction):
        pass

    def show_speed(self):
        print(f'Текущая скорость автомобилья {self.name}: {self.speed}км/ч')


class TownCar(Car):
    MAX_SPEED = 60

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > self.MAX_SPEED:
            print(f'Превышение скорости автомобилем {self.name}!')
        print(f'Текущая скорость автомобилья {self.name}: {self.speed}км/ч')


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
        print(f'Текущая скорость автомобилья {self.name}: {self.speed}км/ч')


class PoliceCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


if __name__ == '__main__':
    pc = PoliceCar(180, 'голубой', 'У209ЕХ28')
    wc1 = WorkCar(12, 'зеленый', 'М456УЕ56')
    wc2 = WorkCar(120, 'белый', 'У315ОЛ65')
    sc = SportCar(200, 'красный', 'shumackher')
    tc1 = TownCar(80, 'серый', 'У400АМ27')
    tc2 = TownCar(60, 'черный', 'O345EX96')
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
