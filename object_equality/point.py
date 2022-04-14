class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return (other is self or
            type(other) == Point and
            self.x == other.x and self.y == other.y)