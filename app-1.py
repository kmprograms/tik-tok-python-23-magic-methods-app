import math

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def distance(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __lt__(self, other):
        return isinstance(other, Point) and self.distance() < other.distance()

    # def __gt__(self, other):
    #     return isinstance(other, Point) and self.distance() > other.distance()

    def __le__(self, other):
        return isinstance(other, Point) and self.distance() <= other.distance()

    # def __ge__(self, other):
    #     return isinstance(other, Point) and self.distance() > other.distance()

    def __eq__(self, other):
        return isinstance(other, Point) and self.distance() == other.distance()

    def __repr__(self):
        return f'({self.x}, {self.y})'


def main() -> None:
    p1 = Point(1, 1)
    p2 = Point(2, 2)
    p3 = Point(3, 3)
    p4 = Point(4, 4)

    print('---------------------------- (1) ----------------------------')
    print(p1 < p2)
    print(p2 < p1)

    print('---------------------------- (2) ----------------------------')
    print(p2 > p1)
    print(p1 > p2)

    print('---------------------------- (3) ----------------------------')
    print(p3 >= p3)
    print(p4 >= p4)

    print('---------------------------- (4) ----------------------------')
    print(p4 <= p4)
    print(p4 <= p3)

    print('---------------------------- (5) ----------------------------')
    points = [Point(3, 1), Point(1, 0), Point(2, 5), Point(2, 3)]

    points.sort()
    print(points)

    points.sort(reverse=True)
    print(points)


if __name__ == '__main__':
    main()
