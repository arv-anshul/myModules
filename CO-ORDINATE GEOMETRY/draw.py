import matplotlib.pyplot as plt


class Draw():
    def init(self):
        pass

    @staticmethod
    def triangle(p1, p2, p3, marker='o'):
        plt.plot([p1.x, p2.x, p3.x, p1.x], [
                 p1.y, p2.y, p3.y, p1.y], marker=marker)

    @staticmethod
    def quadilateral(p1, p2, p3, p4, marker='o'):
        plt.plot([p1.x, p2.x, p3.x, p4.x, p1.x], [
                 p1.y, p2.y, p3.y, p4.y, p1.y], marker=marker)

    @staticmethod
    def polygon(*args, marker='o', c='blue', grid=True):
        if len(args) == 1:
            args[0].plot_point(grid=grid, c=c)
        elif len(args) == 2:
            args[0].plot_graph(args[1], grid=grid)
        else:
            plt.grid(grid)
            plt.plot([*(p.x for p in args), (args[0].x)],
                     [*(p.y for p in args), (args[0].y)], marker=marker, c=c)


def draw_polygon(*args, marker='o', c='blue', grid=True):
    """draw_polygon : Draw n-vertex polygon in 2D plane with matplotlib library.

    Args:
        marker (str, optional): Marker for points. Defaults to 'o'.
        c (str, optional): Color for lines and points. Defaults to 'blue'.
        grid (bool, optional): Apply grid in graph. Defaults to True.
    """
    if len(args) == 1:
        args[0].plot_point(grid=grid, c=c)
    elif len(args) == 2:
        args[0].plot_graph(args[1], grid=grid)
    else:
        plt.grid(grid)
        plt.plot([*(p.x for p in args), (args[0].x)],
                 [*(p.y for p in args), (args[0].y)], marker=marker, c=c)
