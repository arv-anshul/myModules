from matplotlib import pyplot as plt


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
        """draw : Draw the triangle and tells you the the type of it.

        Args:
            marker (str, optional): Shape of point. Defaults to 'o'.
            grid (bool, optional): Display grid in graph. Defaults to True.
        """
        plt.grid(grid)

        title = self.which_triangle()
        plt.title(title)

        # points plotting
        plt.scatter(self.A.x, self.A.y, marker=marker, label=f'A: {self.A.x, self.A.y}')
        plt.scatter(self.B.x, self.B.y, marker=marker, label=f'B: {self.B.x, self.B.y}')
        plt.scatter(self.C.x, self.C.y, marker=marker, label=f'C: {self.C.x, self.C.y}')

        plt.plot([self.A.x, self.B.x, self.C.x, self.A.x],
                 [self.A.y, self.B.y, self.C.y, self.A.y])

        plt.legend()
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.text(-0.5, -0.5, '(0, 0)', color='grey')
        plt.axhline(color='k')
        plt.axvline(color='k')

    def which_triangle(self):
        """which_triangle : Tells you the type of triangle.
        i.e. 'Equilateral', 'Isosceles', 'Scalene'.

        Returns:
            str: 'Equilateral', 'Isosceles', 'Scalene'
        """
        AB = self.A.euclidianDistance(self.B)
        BC = self.B.euclidianDistance(self.C)
        AC = self.A.euclidianDistance(self.C)

        if AB==BC==AC:
            return 'Equilateral Triangle'
        elif (AB==BC) or (BC==AC) or (AC==AB):
            return 'Isosceles Triangle'
        else:
            return 'Scalene Triangle'


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
        """draw : Draw the quailateral and tells you the the type of it.

        Args:
            diagonal (bool, optional): Display the diagonal of the quailateral. Default to True.
            marker (str, optional): Shape of pointer. Defaults to 'o'.
            grid (bool, optional): Display grid in graph. Defaults to True.
        """
        plt.grid(grid)

        title = self.which_quadilateral()
        plt.title(title)

        # points plotting
        plt.scatter(self.A.x, self.A.y, marker=marker, label=f'A: {self.A.x, self.A.y}')
        plt.scatter(self.B.x, self.B.y, marker=marker, label=f'B: {self.B.x, self.B.y}')
        plt.scatter(self.C.x, self.C.y, marker=marker, label=f'C: {self.C.x, self.C.y}')
        plt.scatter(self.D.x, self.D.y, marker=marker, label=f'C: {self.D.x, self.D.y}')

        plt.plot([self.A.x, self.B.x, self.C.x, self.D.x, self.A.x],
                 [self.A.y, self.B.y, self.C.y, self.D.y, self.A.y])

        # Draw diagonal
        if diagonal:
            plt.plot([self.A.x, self.C.x], [self.A.y, self.C.y], c='orange', linestyle='dashed')
            plt.plot([self.B.x, self.D.x], [self.B.y, self.D.y], c='orange', linestyle='dashed')

        plt.legend()
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.text(-0.5, -0.5, '(0, 0)', color='grey')
        plt.axhline(color='k')
        plt.axvline(color='k')

    def which_quadilateral(self):
        """which_triangle : Tells you the type of triangle.
        i.e. Square, Rectangle, Rhombus, Parallelogram

        Returns:
            str: Square, Rectangle, Rhombus, Parallelogram
        """
        AB = self.A.euclidianDistance(self.B)
        BC = self.B.euclidianDistance(self.C)
        CD = self.C.euclidianDistance(self.D)
        AD = self.A.euclidianDistance(self.D)

        if AB==BC==CD==AD:
            return 'Rhombus' if self.is_rhombus() else 'Square'
        elif AB==CD and BC==AD:
            return 'Parallelogram' if self.is_llgm() else 'Rectangle'
        else: 
            return 'Nothing'

    def is_llgm(self):
        """is_llgm : Determines whether given quailateral is llgm or not.

        Returns:
            bool: Whether quailateral is llgm or not.
        """
        mid_1 = self.A.mid_point(self.C)
        mid_2 = self.B.mid_point(self.D)

        return True if mid_1 == mid_2 else False

    def is_rhombus(self):
        """is_rhombus : Determines whether given quailateral is rhombus or not.

        Returns:
            bool: Whether quailateral is rhombus or not.
        """
        d1 = self.A.euclidianDistance(self.C)
        d2 = self.B.euclidianDistance(self.D)
        return True if d1!=d2 else False


class Polygon():
    """A class to perform some calculation on 2D Polygons."""
    def __init__(self, *args) -> None:
        pass