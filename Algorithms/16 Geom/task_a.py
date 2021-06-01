"""Task A Solution"""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Vector:
    def __init__(self, a, b):
        self.x = b.x - a.x
        self.y = b.y - a.y

    def scalar_product(self, other):
        return self.x * other.x + self.y * other.y

    def vector_product(self, other):
        return self.x * other.y - self.y * other.x

class Segment:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def contains(self, c):
        v1 = Vector(self.a, c)
        v2 = Vector(self.b, c)
        scalar_product = v1.scalar_product(v2)
        vector_product = v1.vector_product(v2)
        if scalar_product <= 0 and vector_product == 0:
            return True
        else:
            return False

if __name__ == '__main__':
    c_x, c_y, a_x, a_y, b_x, b_y = map(int, input().split())
    s = Segment(Point(a_x, a_y), Point(b_x, b_y))
    if s.contains(Point(c_x, c_y)):
        print('YES')
    else:
        print('NO')