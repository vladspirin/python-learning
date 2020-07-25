class Point:
    def __init__(self, x, y):
        self.x = abs(x)
        self.y = abs(y)

    def dist(self, pt):
        return ((pt.x - self.x) ** 2 + (pt.y - self.y) ** 2) ** 0.5

p1 = Point(1.5, 1)
p2 = Point(1.5, 2)

print(p1.dist(p2))