import math
class Line:

    def __init__(self, coor1, coor2):
        self.x1, self.y1 = coor1
        self.x2, self.y2 = coor2

    def distance(self):
        return math.sqrt(pow(self.x2 - self.x1, 2) - pow(self.y2 - self.y1, 2))

    def slope(self):
        pass