# ====================
# 라이브러리
# ====================
import math

# ====================
#   상수
# ====================
G = 6.674e-11

# ====================
#   class
# ====================
class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class CelestialBody:
    def __init__(self, name, mass, radius, pos, v, color):
        self.name = name
        self.mass = mass
        self.radius = radius
        self.pos = pos
        self.v = v
        self.color = color

    def get_gravity(self, m1, m2):
        pass

    def get_distance(self, pos1, pos2):
        result = 0

        x1 = pos1.x
        y1 = pos1.y
        x2 = pos2.x
        y2 = pos2.y

        result = math.sqrt((x2-x1)**2 + (y2-y1)**2)

        return result



