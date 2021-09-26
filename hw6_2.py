#2. Реализовать класс Road (дорога), в котором определить атрибуты:
#length (длина), width (ширина).
#Значения данных атрибутов должны передаваться при создании
#экземпляра класса. Атрибуты сделать защищенными.
#Определить метод расчета массы асфальта, необходимого
#для покрытия всего дорожного полотна.
#Использовать формулу: длина*ширина*масса асфальта
#для покрытия одного кв метра дороги асфальтом, толщиной
#в 1 см*число см толщины полотна. Проверить работу метода.
#Например: 20м*5000м*25кг*5см = 12500 т

# если все атрибуты передаются при создании экземпляра
class Road():
    _length: int
    _width: int

    def __init__(self, _length, _width, mass, thickness):  # конструктор для приема переменных экземпляров
        self._length = _length
        self._width = _width
        self.thickness = thickness
        self.mass = mass

    def weight_asf(self):
        return (self._length * self._width * self.mass * (self.thickness / 100)) * 0.1

m = Road(25, 6000, 25, 5)  # экземпляр
print(f'Масса асфальта: {m.weight_asf()} тонн')


# если при создании экземпляра передаются только длина и ширина
class Road():
    _length: int
    _width: int

    def __init__(self, _length, _width):  # конструктор для приема переменных экземпляров
        self._length = _length
        self._width = _width

    def weight_asf(self):
        mass = 25
        thickness = 5
        return (self._length * self._width * mass * (thickness / 100)) * 0.1


m = Road(25, 6000)  # экземпляр
print(f'Масса асфальта: {m.weight_asf()} тонн')