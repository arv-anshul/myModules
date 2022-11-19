class Cartesian_3D:
    def __init__(self, x, y, z) -> None:
        """Repersent a point on 3D plane.

        Args:
            x (int | float): X co-ordinate.
            y (int | float): Y co-ordinate.
            z (int | float): Z co-ordinate.
        """
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
        return f'({self.x}, {self.y}, {self.z})'

    def __eq__(self, __o) -> bool:
        return True if self.x == __o.x and self.y == __o.y and self.z == __o.z else False
