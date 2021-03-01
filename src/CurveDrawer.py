from matplotlib.pyplot import plot, show, savefig


class CurveDrawer:
    def __init__(self, xCoors, yCoors):
        self.xCoors = xCoors
        self.yCoors = yCoors

    def draw(self):
        plot(self.xCoors, self.yCoors)
        show()
        savefig('graph.pdf')
        savefig('graph.png')
