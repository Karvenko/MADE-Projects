"""Task F solution"""
import math

class Xerox:
    """Class to store xerox info"""
    def __init__(self, n_pages, t_x, t_y):
        self.n_pages = n_pages
        self.t_x = min(t_x, t_y) #Always fastest
        self.t_y = max(t_x, t_y) #Always slowest 


    def get_value(self, n):
        """Calc copy time if n pages sent to xerox 1"""
        return max(round(n) * self.t_x, (self.n_pages - round(n)) * self.t_y + self.t_x)


def find_min(func, low, up):
    """Find minimum with triple section"""
    if up - low <= 1:
        return min(func(low), func(up))

    tmp_low = low
    tmp_up = up
    m1 = (tmp_up - tmp_low) // 2 + tmp_low
    m2 = m1 + 1
    f1 = func(m1)
    f2 = func(m2)

    while tmp_up - tmp_low > 2:
        if f1 < f2:
            tmp_up = m2
        else:
            tmp_low = m1
        m1 = (tmp_up - tmp_low) // 2 + tmp_low
        m2 = m1 + 1
        f1 = func(m1)
        f2 = func(m2)

    middle = (tmp_up - tmp_low) // 2 + tmp_low

    return min(func(tmp_low), func(tmp_up), func(middle))


if __name__ == '__main__':
    n_pages, t_x, t_y = map(int, input().split())

    xerox = Xerox(n_pages, t_x, t_y)
    print(find_min(xerox.get_value, 1, n_pages))
