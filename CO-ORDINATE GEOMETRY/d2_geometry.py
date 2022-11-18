import matplotlib.pyplot as plt
import numpy as np


class Cartesian_2D():
    def __init__(self, x, y):
        self.x = x
        self.y = y

        # variables
        self.distance_from_origin_ = float((self.x**2 + self.y**2))**0.5

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'

    def __eq__(self, __o: object) -> bool:
        return True if self.x == __o.x and self.y == __o.y else False

    def euclidianDistance(self, __o):
        temp_x = (self.x - __o.x)**2
        temp_y = (self.y - __o.y)**2
        return (temp_x + temp_y)**0.5

    def slope(self, __o):
        temp_x = (__o.x - self.x)
        temp_y = (__o.y - self.y)
        return temp_y/temp_x if temp_x != 0 else 99999

    def mid_point(self, __o):
        temp_x = (self.x + __o.x) / 2
        temp_y = (self.y + __o.y) / 2
        return Cartesian_2D(temp_x, temp_y)

    def section_formula(self, __o, m, n):
        temp_x = float((n * self.x)+(m * __o.x))/(m + n)
        temp_y = float((n * self.y)+(m * __o.y))/(m + n)
        return Cartesian_2D(temp_x, temp_y)

    def which_quadrant(self):
        if self.x == 0:
            return 'On Y-axis'
        elif self.y == 0:
            return 'On X-axis'
        else:
            if self.x > 0:
                return 1 if self.y > 0 else 4
            else:
                return 2 if self.y > 0 else 3

    def plot_point(self, grid=True, c='blue'):
        ax = plt.figure()
        plt.grid(grid)

        # graph title --> quadrant
        title = self.which_quadrant()
        plt.title(f'{title} Quadrant') if isinstance(
            title, int) else plt.title(title)

        # set axis limit
        if self.x != 0 and self.y != 0:
            plt.xlim(0, self.x*1.5)
            plt.ylim(0, self.y*1.5)
        else:
            zx = ax.gca()
            zx.spines['left'].set_position('zero')
            zx.spines['bottom'].set_position('zero')

        # graph line
        plt.plot([self.x, self.x], [0, self.y], c=c)
        plt.plot([0, self.x], [self.y, self.y], c=c)

        plt.scatter(self.x, self.y, c=c, marker='o',
                    label=f'({self.x}, {self.y})')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.legend()

    def __plot_point(self, c='blue', label=None):
        plt.scatter(self.x, self.y, c=c, label=label)

    def plot_graph(self, __o, m=None, n=None, grid=True):
        ax = plt.figure()
        plt.grid(grid)

        # graph title
        plt.title('')

        # display co-ordinates point
        plt.scatter(self.x, self.y, c='blue',
                    label=f'(x1, y1): {self.x, self.y}')
        plt.scatter(__o.x, __o.y, c='red', label=f'(x2, y2): {__o.x, __o.y}')

        # joining line
        plt.plot([self.x, __o.x], [self.y, __o.y], c='k')

        # section formula
        if m is not None and n is None:
            print('Please enter both m and n.')
        elif m and n:
            sf = self.section_formula(__o, m, n)
            sf.__plot_point(
                c='green', label=f'(m, n): {np.round(sf.x,1), np.round(sf.y, 1)}')

        plt.legend()
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.axhline(color="black")
        plt.axvline(color="black")
        plt.text(-0.5, -0.5, '(0, 0)', color='grey')


def angle_between(A, O, B):
    """angle_between : Return ∠AOB of given two line-segment.

    Args:
        A (Cartesian_2D): Co-ordinate.
        O (Cartesian_2D): Co-ordinate.
        B (Cartesian_2D): Co-ordinate.

    Returns:
        tuple(int, int): (acute, obtuse) or (θ, 180-θ)
    """
    m1 = A.slope(O)
    m2 = B.slope(O)

    if m1 == m2:
        return 0, 180
    elif m1*m2 == -1:
        return 90, 90
    else:
        tan = (m2-(m1))/(1+(m1)*m2)
        acute = np.round(np.degrees(np.arctan(abs(tan))), 3)
        obtuse = np.round(np.degrees(np.pi-np.arctan(abs((m2-(m1))/(1+(m1)*m2)))), 3)
        return acute, obtuse


def is_parallel(*lines):
    pass
