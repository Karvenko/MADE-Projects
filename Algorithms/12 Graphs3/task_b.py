"""Task B solution"""
import sys

class SNM:
    def __init__(self, n):
        self.n = n
        self.rank = [0] * n
        self.parents = [0] * n
        # self.min = [0] * n
        # self.max = [0] * n
        self.rating = [0] * n
        self.count = [1] * n
        # self.update = [False] * n
        for i in range(n):
            self.parents[i] = i
            # self.min[i] = i
            # self.max[i] = i

    def print_snm(self):
        print(f'size: {self.n}')
        print(f'ranks: {self.rank}')
        print(f'parents: {self.parents}')
        # print(f'min: {self.min}')
        print(f'rating: {self.rating}')
        print(f'count: {self.count}')
        # print(f'updates: {self.update}')

    def get(self, x):
        next = self.parents[x]
        while self.parents[x] != self.parents[next]:
            self.rating[x] += self.rating[next]
            self.parents[x] = self.parents[next]
            x = next
            next = self.parents[next]

        if x == next:
            # self.rating[x] += self.rating[next]
            return self.parents[next], self.rating[next]
        else:
            return self.parents[next], self.rating[x] + self.rating[next]

    def get_rating(self, x):
        p, r = self.get(x)
        return r

    def join(self, x, y):
        orig_x = x
        orig_y = y
        x, _ = self.get(x)
        y, _ = self.get(y)
        if x == y:
            return
        if self.rank[x] > self.rank[y]:
            x, y = y, x
        if self.rank[x] == self.rank[y]:
            self.rank[y] += 1

        self.parents[x] = y
        self.rating[x] -= self.rating[y]
        # self.max[y] = max(self.max[x], self.max[y])
        # self.min[y] = min(self.min[x], self.min[y])
        # self.count[y] += self.count[x]
        _, _ = self.get(orig_x)
        _, _ = self.get(orig_y)
        _, _ = self.get(x)

    def add(self, x, val):
        p, r = self.get(x)
        self.rating[p] += val

if __name__ == '__main__':
    data = sys.stdin.readlines()
    n, m = map(int, data[0].split())
    result = []
    s = SNM(n)
    for line in data[1:]:
        if line[0] == 'j':
            x, y = map(int, line.split()[1:])
            s.join(x - 1, y - 1)
        elif line[0] == 'a':
            x, val = map(int, line.split()[1:])
            s.add(x - 1, val)
        else:
            tmp = s.get(int(line.split()[1]) - 1)[1]
            result.append(str(tmp))
    sys.stdout.write('\n'.join(result))