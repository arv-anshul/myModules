

class Cartesian_3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
        return f'({self.x}, {self.y}, {self.z})'
