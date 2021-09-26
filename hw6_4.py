# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы:
# go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    name: str
    color: str
    speed: int
    is_police: bool

    def __init__(self, name, color, speed, is_police):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        return f'начал движение'

    def stop(self):
        return f'остановился'

    def turn_r(self):
        return f'повернул направо'

    def turn_l(self):
        return f'повернул налево'

    def show_speed(self):
        return self.speed

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'превысил скорость'
        else:
            return self.speed

class SportCar(Car):
    def sport_car(self):
        return f'- sport car.'

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'превысил скорость'
        else:
            return self.speed

class PoliceCar(Car):
    def ispolice(self):
        if self.is_police is True:
            return "- police car."

toyota = TownCar("Toyota", "Red", 80, False)
kamaz = WorkCar("Kamaz", "Orange", 40, False)
porsche = SportCar("Porsche", "Yellow", 150, False)
skoda = PoliceCar("Police Car", "Black", 100, True)

print(f'Марка городского авто: {toyota.name}.\nЦвет рабочей машины: {kamaz.color}. \nСкорость спортивного авто: {porsche.speed}км/ч.\nSkoda - полицейский автомобиль: {skoda.is_police}.')
print(f'Porsche {porsche.sport_car()}\nPorsche {porsche.go()} и {porsche.turn_r()}.')
print(f'Porsche {porsche.show_speed()} и {porsche.stop()}.')
print(f'Toyota {toyota.show_speed()} и {toyota.stop()}.')
print(f'Kamaz {kamaz.turn_r()} и его скорость составляет сейчас {kamaz.show_speed()}км/ч.')
print(f'Skoda {skoda.ispolice()}')

