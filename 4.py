class Car:

    def __init__(self,speed,color,name,is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f'Новая машина: {self.name} (Цвет{self.color}) машина полицейская - {self.is_police}')

    def go(self):
        print(f'{self.name} начал движение')

    def stop(self):
        print(f'{self.name} остановился')

    def turn(self,direction):
        print(f"{self.name}: Машина повернула {'налево' if direction ==0 else 'направо'}")

    def show_speed(self):
        print(f'{self.name}: Скорость автомобиля - {self.speed}')

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name} превысил скорость')
        else:
            return self.speed

class SportCar(Car):
    def sport_car(self):
        print(f'{self.name} спортивный автомобиль')

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'{self.name} превысил скорость')
        else:
            print(f'{self.name}: Скорость автомобиля - {self.speed}')

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
      f'Ferrari {ferrari.go()} и {ferrari.turn(0)}.')
print(f'Lada {lada.show_speed()} и {lada.stop()}.')
print(f'Kamaz {kamaz.turn(1)} и его скорость составляет сейчас {kamaz.show_speed()}км/ч.')
print(f'Ford  {ford .ispolice()}')