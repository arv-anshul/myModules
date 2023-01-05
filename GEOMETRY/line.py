""" Module to represent a line on a 2D plane. 
    All lines are written by ChatGPT.
"""


from typing import Self
from d2_geometry import Point


class LineFromEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self) -> str:
        return f'{self.a} + {self.b} + {self.c} = 0'

    def __repr__(self) -> str:
        return f'Line({self.a}, {self.b}, {self.c})'

    def distance_from_origin(self):
        return abs(self.c) / ((self.a**2 + self.b**2)**0.5)

    def is_parallel(self, other):
        return self.a * other.b == self.b * other.a

    def intersection(self, other):
        if self.is_parallel(other):
            return None
        x = ((other.c * self.b - self.c * other.b) /
             (other.a * self.b - self.a * other.b))
        y = ((self.c * other.a - other.c * self.a) /
             (other.a * self.b - self.a * other.b))
        return Point(x, y)

    def to_point(self):
        if self.a == 0:
            return Point(0, -self.c / self.b)
        elif self.b == 0:
            return Point(-self.c / self.a, 0)
        else:
            return Point(0, -self.c / self.b)

    def to_points(self):
        if self.a == 0:
            x = -self.c / self.b
            return Point(x, 0), Point(x, 1)
        elif self.b == 0:
            y = -self.c / self.a
            return Point(0, y), Point(1, y)
        else:
            y1 = -self.c / self.b
            y2 = -(self.a + self.c) / self.b
            return Point(0, y1), Point(1, y2)


class LineFromPoint:
    def __init__(self, A: Point, B: Point) -> None:
        self.__a = A
        self.__b = B

    @property
    def A(self):
        return self.__a

    @A.setter
    def A(self, value):
        self.__a = value

    @property
    def B(self):
        return self.__b

    @B.setter
    def B(self, value):
        self.__b = value

    def slope(self):
        """Calculate the slope of the line."""
        x_diff = self.__b.x - self.__a.x
        y_diff = self.__b.y - self.__a.y
        if x_diff == 0:
            return None
        return y_diff / x_diff

    @staticmethod
    def check_colinear(*lines) -> bool:
        if len(lines) < 2:
            raise ValueError(
                'Please pass more than one line to check colinearity.')
        result = [False, False]
        for i in range(len(lines)-1):
            result[0] = ((lines[i].__a.x == lines[i+1].__b.x)
                         or (lines[i].__a.y == lines[i+1].__b.y))
            result[1] = lines[i].slope() == lines[i+1].slope()
        return result[0] and result[1]

    @property
    def y_intercept_(self):
        """Calculate the y-intercept of the line."""
        return self.__a.y - self.slope() * self.__a.x

    def x_intercept_(self):
        """ Calculate the x-intercept of the line."""
        if self.slope() == 0:
            return None
        return -self.y_intercept_ / self.slope()

    def is_parallel(self, other: Self):
        """Determine whether the line is parallel to another line."""
        return self.slope() == other.slope()

    def intersection(self, other: Self):
        """Calculate the intersection point of the line with another line, if it exists."""
        if self.slope() is None or other.slope() is None:
            return None
        elif self.is_parallel(other):
            return None
        else:
            x = ((other.y_intercept_ - self.y_intercept_) /
                 (self.slope() - other.slope()))
            y = self.slope() * x + self.y_intercept_
            return Point(x, y)


if __name__ == '__main__':
    A, B = Point(-2, -1), Point(4, 0)
    C, D = Point(3, 3), Point(-3, 2)
    l1 = LineFromPoint(A, B)
    l2 = LineFromPoint(C, D)
    l3 = LineFromPoint(C, B)
    l4 = LineFromPoint(A, D)

    print(LineFromPoint.check_colinear(l1, l2))
