from math import pi, sin, cos


class Point:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z


class Ellipse:
    def __init__(self, centre: Point, radius1: float, radius2: float):
        self.centre = centre
        self.radius_x = radius1
        self.radius_y = radius2

    def is_point_inside(self, point: Point) -> bool:
        return (point.x - self.centre.x)**2 / self.radius_x**2 + (point.y - self.centre.y)**2 / self.radius_y**2 <= 1

    def get_n_points(self, n):
        poins_of_ellipse = []
        step = 2*pi / n

        for j in range(n):
            x = self.radius_x * cos((step * j))
            y = self.radius_y * sin((step * j))
            poins_of_ellipse.append((x, y))

        return poins_of_ellipse

