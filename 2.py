class Road:
    def __init__(self, length, width,weigth,thickness):
        self.length = length
        self.width = width
        self.weigth = weigth
        self.thickness = thickness
    def mass(self):
        mass = self.length * self.width * self.weigth * self.thickness / 1000

road = Road(100000,20, 25,0.05)
print(f'Для построения дороги требуется {road.mass()} тонн асфальта')

