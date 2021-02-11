from math import pi
from math import pow
from math import floor

class Cylinder():
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return pi*pow(self.radius, 2)*self.height

    def surface_area(self):
        return 2*pi*self.radius*self.height + 2*pi*pow(self.radius, 2)


c = Cylinder(2, 3)
print(c.volume()) # 56.548667764616276
print(c.surface_area()) # 94.24777960769379