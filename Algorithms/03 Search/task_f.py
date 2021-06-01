"""Task F solution"""
import math

GOLDEN = (math.sqrt(5) - 1) / 2
EPS = 1e-15

class Field:
    """Class to store field info"""
    def __init__(self, a, v_p, v_f):
        self.a = a
        self.v_p = v_p
        self.v_f = v_f


    def get_value(self, x0):
        """Calc travel time if enter forest in point x0"""
        length_p = math.sqrt(x0 ** 2 + (1 - self.a) ** 2)
        length_f = math.sqrt((1 - x0) ** 2 + self.a ** 2)

        return length_p / self.v_p + length_f / self.v_f


def find_min(func, low, up):
    """Find minimum with triple section using golden"""
    n_iter = math.ceil(math.log2((up - low) / EPS) / math.log2(GOLDEN + 1))

    tmp_low = low
    tmp_up = up
    m1 = (up - low) * (1 - GOLDEN) + low
    m2 = (up - low) * GOLDEN + low
    f1 = func(m1)
    f2 = func(m2)

    for _ in range(n_iter):
        if f1 < f2:
            tmp_up = m2
            m2 = m1
            f2 = f1
            m1 = (tmp_up - tmp_low) * (1 - GOLDEN) + tmp_low
            f1 = func(m1)
        else:
            tmp_low = m1
            m1 = m2
            f1 = f2
            m2 = (tmp_up - tmp_low) * GOLDEN + tmp_low
            f2 = func(m2)

    return m1


if __name__ == '__main__':
    v_p, v_f = map(float, input().split())
    a = float(input())

    field = Field(a, v_p, v_f)
    print(find_min(field.get_value, 0, 1))
