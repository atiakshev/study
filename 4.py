class Car:
    name: str
    color: str
    speed: int
    is_police: bool

    def __init__(self,speed,color,name,is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} начал движение'

    def stop(self):
        return f'{self.name} остановился'

    def turn_right(self):
        return f'{self.name} повернул направо'

    def turn_left(self):
        return f'{self.name} повернул налево'

    def show_speed(self):
        return f'Скорость {self.name} составила {self.speed}'

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


lada = TownCar( 80, 'Red', 'Lada', False)
kamaz = WorkCar(50,'Orange','Kamaz', False)
ferrari = SportCar(180,'Yellow','Ferrari', False)
ford = PoliceCar(100,'Dark','Ford', True)

print(f'Марка городского авто: {lada.name}.\n'
      f'Цвет рабочей машины: {kamaz.color}. \n'
      f'Скорость спортивного авто: {ferrari.speed}км/ч.\n'
      f'Форд - полицейский автомобиль: {ford.is_police}.')
print(f'Ferrari {ferrari.sport_car()}\n'
      f'Ferrari {ferrari.go()} и {ferrari.turn_left()}.')
print(f'Lada {lada.show_speed()} и {lada.stop()}.')
print(f'Kamaz {kamaz.turn_right()} и его скорость составляет сейчас {kamaz.show_speed()}км/ч.')
print(f'Ford  {ford .ispolice()}')