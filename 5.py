class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
       print( f'Запуск отрисовки {self.title}')


class Pen(Stationary):
    def draw(self):
        print( f'Вы взяли {self.title}. Запуск отрисовки ручкой')

class Pencil(Stationary):
    def draw(self):
        print( f'Вы взяли {self.title}. Запуск отрисовки карандашом')

class Marker(Stationary):
    def draw(self):
        print( f'Вы взяли {self.title}. Запуск отрисовки маркером')

pen = Pen('Ручка')
pencil = Pencil('Карандаш')
marc = Marker('Маркер')

pen.draw()
pencil.draw()
marc.draw()
