from typing import Self
import matplotlib.pyplot as plt
import numpy as np


class Point():
    """A class for creating co-ordinate on 2D plane."""

    def __init__(self, x, y) -> None:
        """Repersent a point on 2D plane.

        Args:
            x (int, float): Repersent X ordinate.
            y (int, float): Repersent Y co-ordinate.
        """
        self.x = x
        self.y = y

        # instance variables
        self.distance_from_origin_ = float((self.x**2 + self.y**2))**0.5

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'

    def __eq__(self, __o: Self) -> bool:
        return True if self.x == __o.x and self.y == __o.y else False

    def euclidianDistance(self, __o) -> int | float:
        """Returns the Euclidian distance between two co-ordinate.

        Args:
            __o (Point): Co-ordinate of other point.

        Returns:
            int | float: Distance between two co-ordinate.
        """
        temp_x = (self.x - __o.x)**2
        temp_y = (self.y - __o.y)**2
        return (temp_x + temp_y)**0.5

    def slope(self, __o) -> int | float:
        """Returns slope of line-segment.

        Args:
            __o (Point): Co-ordinate of other point.

        Returns:
            int | float: Slope of line-segment.
        """
        temp_x = (__o.x - self.x)
        temp_y = (__o.y - self.y)
        return temp_y/temp_x if temp_x != 0 else 99999

    def mid_point(self, __o):
        """Return the mid-point co-ordinate between two points in 2D plane.

        Args:
            __o (Point): Co-ordinate of other point.

        Returns:
            Point: Co-ordinate of mid-point.
        """
        temp_x = (self.x + __o.x) / 2
        temp_y = (self.y + __o.y) / 2
        return Point(temp_x, temp_y)

    def section_formula(self, __o, m, n):
        """Break the line-segment into given sections and Return the co-ordinate of breakpoint.

        Args:
            __o (Point): Co-ordinate of other point.
            m (int): First section of the line.
            n (int): Second section of the line.

        Returns:
            Point: Co-ordinate of breakpoint.
        """
        temp_x = float((n * self.x)+(m * __o.x))/(m + n)
        temp_y = float((n * self.y)+(m * __o.y))/(m + n)
        return Point(temp_x, temp_y)

    def which_quadrant(self) -> int | str:
        """Return the quadrant in which the co-ordinate lies.

        Returns:
            int | str: Quadrant as [1,2,3,4] or Axis as ['On Y-axis', 'On X-axis'].
        """
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
        """Plot point on graph with matplotlib library.

        Args:
            grid (bool, optional): Display the grid in graph. Defaults to True.
            c (str, optional): Color of lines. Defaults to 'blue'.
        """
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
        """Plot line-segment on graph. Also, plot the breakpoint using section formula.

        Args:
            __o (Cartesian-2D): Co-ordinate of other point.
            m (int, optional): First section of line. Defaults to None.
            n (int, optional): Second section of line. Defaults to None.
            grid (bool, optional): Display grids. Defaults to True.
        """
        ax = plt.figure()
        plt.grid(grid)

        # graph title
        plt.title('')

        # display co-ordinate point
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
    """Return ∠AOB of given two line-segment.

    Args:
        A (Point): Co-ordinate.
        O (Point): Co-ordinate.
        B (Point): Co-ordinate.

    Returns:
        tuple(float, float): (acute, obtuse) or (θ, 180°-θ)
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
        obtuse = np.round(np.degrees(
            np.pi-np.arctan(abs((m2-(m1))/(1+(m1)*m2)))), 3)
        return acute, obtuse
