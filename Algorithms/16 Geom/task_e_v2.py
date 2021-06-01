"""Task E Solution"""
import sys
from functools import cmp_to_key
from math import sqrt

INF = 10 ** 7

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def squared_dist(self):
        return self.x * self.x + self.y * self.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y

class Vector:
    def __init__(self, a, b):
        self.x = b.x - a.x
        self.y = b.y - a.y

    def scalar_product(self, other):
        return self.x * other.x + self.y * other.y

    def vector_product(self, other):
        return self.x * other.y - self.y * other.x

    def squared_len(self):
        return self.x * self.x + self.y * self.y

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

    def square(self):
        s = 0
        p = self.vl[0]
        for i in range(1, len(self.vl) - 1):
            v1 = Vector(p, self.vl[i])
            v2 = Vector(p, self.vl[i + 1])
            s += v1.vector_product(v2)
        return abs(s / 2)

    def perimetr(self):
        p = 0
        for i in range(1, len(self.vl)):
            p += sqrt(Vector(self.vl[i - 1], self.vl[i]).squared_len())
        p += sqrt(Vector(self.vl[0], self.vl[-1]).squared_len())
        return p

def point_cmp(a: Point, b: Point):
    """Compares polar angles of two points. if angles are the same - lower length is less"""
    v_p = a.x * b.y - a.y * b.x
    if v_p > 0:
        return -1
    elif v_p < 0:
        return 1
    else:
        sl_a = a.squared_dist()
        sl_b = b.squared_dist()
        if sl_a < sl_b:
            return -1
        elif sl_a > sl_b:
            return 1
        else:
            return 0

def find_start_point(points):
    """Returns index of lower left point"""
    min_x = INF
    min_y = INF
    min_index = -1
    for idx, p in enumerate(points):
        if p.y < min_y:
            min_y = p.y
            min_x = p.x
            min_index = idx
        elif p.y == min_y and p.x < min_x:
            min_x = p.x
            min_index = idx
    return min_index

def shift_points(points, shift):
    points = [p - shift for p in points]
    return points

def find_convex_hull(points):
    start_point = points[find_start_point(points)]
    points = shift_points(points, start_point)
    points = sorted(points, key=cmp_to_key(point_cmp))
    convex_hull = points[:2]
    for p in points[2:]:
        v1 = Vector(convex_hull[-2], convex_hull[-1])
        v2 = Vector(convex_hull[-1], p)
        p_v1_v2 = v1.vector_product(v2)
        while p_v1_v2 <= 0 and len(convex_hull) > 2:
            convex_hull.pop()
            v1 = Vector(convex_hull[-2], convex_hull[-1])
            v2 = Vector(convex_hull[-1], p)
            p_v1_v2 = v1.vector_product(v2)
        convex_hull.append(p)
    return convex_hull

if __name__ == '__main__':
    vertex_set = set()
    data = sys.stdin.readlines()
    for line in data[1:]:
        x, y = map(int, line.split())
        vertex_set.add((x, y))
    vertex_list = [Point(x[0], x[1]) for x in vertex_set]
    convex_hull = find_convex_hull(vertex_list)
    poly = Polygon(convex_hull)
    result = poly.perimetr()
    print(result)