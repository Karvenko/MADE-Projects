"""Task B Solution"""

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

    def intersects(self, other):
        v_ab = Vector(self.a, self.b)
        v_ac = Vector(self.a, other.a)
        v_ad = Vector(self.a, other.b)
        v_cd = Vector(other.a, other.b)
        v_ca = Vector(other.a, self.a)
        v_cb = Vector(other.a, self.b)

        p_ab_ac = v_ab.vector_product(v_ac)
        p_ab_ad = v_ab.vector_product(v_ad)
        p_cd_ca = v_cd.vector_product(v_ca)
        p_cd_cb = v_cd.vector_product(v_cb)

        if p_ab_ac == 0 and p_ab_ad == 0 \
                and p_cd_ca == 0 and p_cd_cb == 0:
            if self.contains(other.a) or self.contains(other.b) \
                    or other.contains(self.a) or other.contains(self.b):
                return True
            else:
                return False
        else:
            if p_ab_ac * p_ab_ad <= 0 and p_cd_ca * p_cd_cb <= 0:
                return True
            else:
                return False

if __name__ == '__main__':
    a_x, a_y, b_x, b_y = map(int, input().split())
    c_x, c_y, d_x, d_y = map(int, input().split())
    s1 = Segment(Point(a_x, a_y), Point(b_x, b_y))
    s2 = Segment(Point(c_x, c_y), Point(d_x, d_y))
    if s1.intersects(s2):
        print('YES')
    else:
        print('NO')