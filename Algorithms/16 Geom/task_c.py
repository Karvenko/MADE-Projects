"""Task C Solution"""
import sys

INF = 10 ** 7

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

    def intersects(self, other, exclude_lower=False):
        """If exclude_lower key is True, function will return False
        if lower point of other is on the segment"""
        if exclude_lower:
            point = other.a if other.a.y < other.b.y else other.b
            if self.contains(point):
                return False

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

class Polygon:
    def __init__(self, vertex_list):
        self.vl = vertex_list

    def contains_point(self, p):
        counter = 0
        ray = Segment(p, Point(INF, p.y)) #Horizontal Ray
        for i in range(len(self.vl) - 1):
            cur_seg = Segment(self.vl[i], self.vl[i + 1])
            if cur_seg.contains(p):
                return True
            if ray.intersects(cur_seg, exclude_lower=True):
                counter += 1
        cur_seg = Segment(self.vl[0], self.vl[-1])
        if cur_seg.contains(p):
            return True
        if ray.intersects(cur_seg, exclude_lower=True):
            counter += 1
        return bool(counter % 2)

if __name__ == '__main__':
    vertex_list = []
    data = sys.stdin.readlines()
    _, p_x, p_y = map(int, data[0].split())
    for line in data[1:]:
        x, y = map(int, line.split())
        vertex_list.append(Point(x, y))
    poly = Polygon(vertex_list)
    if poly.contains_point(Point(p_x, p_y)):
        print('YES')
    else:
        print('NO')