from matplotlib import pyplot as plt
from math import pi, sin, cos

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


class Ellipse:
    def __init__(self, centre: Point, radius1: float, radius2: float):
        self.centre = centre
        self.radius_x = radius1
        self.radius_y = radius2

    def isPointInside(self, point: Point) -> bool:
        return (point.x - self.centre.x)**2 / self.radius_x**2 + (point.y - self.centre.y)**2 / self.radius_y**2 <= 1

    def getNpoints(self, n):
        poins_of_ellipse = []
        step = 2*pi / n

        for j in range(n):
            x = self.radius_x * cos((step * j))
            y = self.radius_y * sin((step * j))
            poins_of_ellipse.append((x, y))

        return poins_of_ellipse

# Point
point = Point(-15, 25)

# Ellipse
ellipse_centre_point = Point(0, 0)
ellipse_radius_x = 1
ellipse_radius_y = 2
ellipse = Ellipse(ellipse_centre_point, ellipse_radius_x, ellipse_radius_y)

# Check if P inside E
print(ellipse.isPointInside(point))

# Get 64 points on ellipse
plt.scatter(*zip(*ellipse.getNpoints(64)))
plt.show()
