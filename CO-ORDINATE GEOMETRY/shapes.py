from matplotlib import pyplot as plt
from d2_geometry import angle_between


# Variables and functions
# area of all shapes,

class Polygon():
    """A class to perform some calculation on 2D Polygons."""

    def __init__(self, *args) -> None:
        pass


class Triangle():
    """A class to perform some calculation on 2D triangles."""

    def __init__(self, A, B, C):
        """Takes three arguments which defines the triangle's coordinates.

        Args:
            A (Cartesian_2D): Triangle's coordinate.
            B (Cartesian_2D): Triangle's coordinate.
            C (Cartesian_2D): Triangle's coordinate.
        """
        self.A = A
        self.B = B
        self.C = C

    def draw(self, marker='o', grid=True):
        """Draw the triangle and tells you the the type of it.

        Args:
            marker (str, optional): Shape of point. Defaults to 'o'.
            grid (bool, optional): Display grid in graph. Defaults to True.
        """
        plt.grid(grid)

        plt.title(
            f'{self.which_triangleByAngle()} Angled, {self.which_triangleBySide()} Triangle')

        # points plotting
        plt.scatter(self.A.x, self.A.y, marker=marker,
                    label=f'A: {self.A.x, self.A.y}')
        plt.scatter(self.B.x, self.B.y, marker=marker,
                    label=f'B: {self.B.x, self.B.y}')
        plt.scatter(self.C.x, self.C.y, marker=marker,
                    label=f'C: {self.C.x, self.C.y}')

        plt.plot([self.A.x, self.B.x, self.C.x, self.A.x],
                 [self.A.y, self.B.y, self.C.y, self.A.y])

        plt.legend()
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.text(-0.5, -0.5, '(0, 0)', color='grey')
        plt.axhline(color='k')
        plt.axvline(color='k')

    def which_triangleBySide(self) -> str:
        """Tells you the type of triangle according to sides.

        Returns:
            str: ['Equilateral', 'Isosceles', 'Scalene']
        """
        AB = self.A.euclidianDistance(self.B)
        BC = self.B.euclidianDistance(self.C)
        AC = self.A.euclidianDistance(self.C)

        if AB == BC == AC:
            return 'Equilateral'
        elif (AB == BC) or (BC == AC) or (AC == AB):
            return 'Isosceles'
        else:
            return 'Scalene'

    def which_triangleByAngle(self):
        """Tells you the type of triangle according to angles.

        Returns:
            str: ['Acute', 'Right', 'Obtuse']
        """
        ab2 = (self.A.x - self.B.x)**2 + (self.A.y - self.B.y)**2
        bc2 = (self.B.x - self.C.x)**2 + (self.B.y - self.C.y)**2
        ac2 = (self.C.x - self.A.x)**2 + (self.C.y - self.A.y)**2

        AB, BC, AC = sorted([ab2, bc2, ac2])

        return 'Acute' if AB + BC > AC else 'Right' if AB + BC == AC else 'Obtuse'

    def area(self):
        """Return area of triangle.

        Returns:
            float: Area of triangle.
        """
        area = 0.5 * abs((self.A.x * (self.B.y - self.C.y) +
                          self.B.x * (self.C.y - self.A.y) +
                          self.C.x * (self.A.y - self.B.y)))
        return area


class Quadilateral():
    """A class to perform some calculation on 2D Quadilaterals."""

    def __init__(self, A, B, C, D):
        """Takes four arguments which defines the Quadilateral's coordinates.

        Args:
            A (Cartesian_2D): Quadilateral's coordinate.
            B (Cartesian_2D): Quadilateral's coordinate.
            C (Cartesian_2D): Quadilateral's coordinate.
            D (Cartesian_2D): Quadilateral's coordinate.
        """
        self.A = A
        self.B = B
        self.C = C
        self.D = D

    def draw(self, diagonal=False, marker='o', grid=True):
        """Draw the quailateral and tells you the the type of it.

        Args:
            diagonal (bool, optional): Display the diagonal of the quailateral. Default to True.
            marker (str, optional): Shape of pointer. Defaults to 'o'.
            grid (bool, optional): Display grid in graph. Defaults to True.
        """
        plt.grid(grid)

        title = self.which_quadilateral()
        plt.title(title)

        # points plotting
        plt.scatter(self.A.x, self.A.y, marker=marker,
                    label=f'A: {self.A.x, self.A.y}')
        plt.scatter(self.B.x, self.B.y, marker=marker,
                    label=f'B: {self.B.x, self.B.y}')
        plt.scatter(self.C.x, self.C.y, marker=marker,
                    label=f'C: {self.C.x, self.C.y}')
        plt.scatter(self.D.x, self.D.y, marker=marker,
                    label=f'C: {self.D.x, self.D.y}')

        plt.plot([self.A.x, self.B.x, self.C.x, self.D.x, self.A.x],
                 [self.A.y, self.B.y, self.C.y, self.D.y, self.A.y])

        # Draw diagonal
        if diagonal:
            plt.plot([self.A.x, self.C.x], [self.A.y, self.C.y],
                     c='orange', linestyle='dashed')
            plt.plot([self.B.x, self.D.x], [self.B.y, self.D.y],
                     c='orange', linestyle='dashed')

        plt.legend()
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.text(-0.5, -0.5, '(0, 0)', color='grey')
        plt.axhline(color='k')
        plt.axvline(color='k')

    def which_quadilateral(self):
        """Tells you the type of triangle.
        i.e. Square, Rectangle, Rhombus, Parallelogram

        Returns:
            str: Square, Rectangle, Rhombus, Parallelogram
        """
        AB = self.A.euclidianDistance(self.B)
        BC = self.B.euclidianDistance(self.C)
        CD = self.C.euclidianDistance(self.D)
        AD = self.A.euclidianDistance(self.D)

        if AB == BC == CD == AD:
            return 'Rhombus' if self.__is_rhombus() else 'Square'
        elif AB == CD and BC == AD:
            return 'Parallelogram' if self.__is_llgm() else 'Rectangle'
        else:
            return 'Irregular'

    def __is_llgm(self):
        """Determines whether given quailateral is llgm or not.

        Returns:
            bool: Whether quailateral is llgm or not.
        """
        mid_point_term = self.A.mid_point(self.C) == self.B.mid_point(self.D)
        diagonal_term = self.A.euclidianDistance(
            self.C) != self.B.euclidianDistance(self.D)

        return True if mid_point_term and diagonal_term else False

    def __is_rhombus(self):
        """Determines whether given quailateral is rhombus or not.

        Returns:
            bool: Whether quailateral is rhombus or not.
        """
        diagonal_term = self.A.euclidianDistance(
            self.C) != self.B.euclidianDistance(self.D)
        side_term = self.A.euclidianDistance(self.B) == self.B.euclidianDistance(
            self.C) == self.C.euclidianDistance(self.D) == self.A.euclidianDistance(self.D)

        return True if diagonal_term and side_term else False

    def __is_trapezium(self):
        # Not Working
        m1 = abs(self.A.slope(self.B)) - abs(self.C.slope(self.D)) == 0
        m2 = abs(self.A.slope(self.C)) - abs(self.B.slope(self.D)) == 0

        side_term = self.A.euclidianDistance(
            self.D) == self.B.euclidianDistance(self.C)
        if side_term and (m1 == True and m2 == False) or (m2 == True and m1 == False):
            return True
        else:
            return False

    def area(self):
        """Return area of quadilateral.

        Returns:
            float: Area of quadilateral.
        """
        area = 0.5 * abs(((self.A.x*self.B.y + self.B.x*self.C.y + self.C.x*self.D.y + self.D.x*self.A.y)
                          - (self.B.x*self.A.y + self.C.x*self.B.y + self.D.x*self.C.y + self.A.x*self.D.y)))
        return area
