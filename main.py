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
    def __init__(self, name, mass, radius, pos, vx, vy, color):
        self.name = name
        self.mass = mass
        self.radius = radius
        self.pos = pos
        self.vx = vx
        self.vy = vy
        self.color = color

    def get_acceleration(self, f, m):
        result = f/m
        return result

    def get_gravity(self, m1, m2, r):
        result = ((m1*m2)/(r**2)) * G
        return result

    def get_distance(self, pos1, pos2):
        x1 = pos1.x
        y1 = pos1.y
        x2 = pos2.x
        y2 = pos2.y

        result = math.sqrt((x2-x1)**2 + (y2-y1)**2)
        return result

    def get_next_velocity(self, ax, ay, dt):
        result = [self.vx + ax * dt, self.vy + ay * dt]
        return result

    def get_next_position(self, dt):
        result = Vector2(self.pos.x + self.vx * dt, self.pos.y + self.vy * dt)
        return result

# """

dt = 0.0001

sun = CelestialBody("sun", 1.989e30, 1392684, Vector2(0, 0), 0, "red")
earth = CelestialBody("earth", 5.9722e24, 12756, Vector2(149600000, 149600000), 1000, "blue")

# r = earth.get_distance(earth.pos , sun.pos)
# sans = earth.get_gravity(sun.mass, earth.mass, r)


def update():
    r = earth.get_distance(sun.pos, earth.pos)
    f = earth.get_gravity(earth.mass, sun.mass, r)
    a = earth.get_acceleration(f, earth.mass)
    ux = earth.get_next_velocity(a, dt)
    earth.v = u
    earth.pos = earth.get_next_position(dt)
    
    print(earth.pos.x, earth.pos.y)

for i in range(30):
    update()

# """
