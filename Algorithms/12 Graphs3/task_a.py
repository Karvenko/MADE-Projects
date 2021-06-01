"""Task A solution"""
import sys

class SNM:
    def __init__(self, n):
        self.n = n
        self.rank = [0] * n
        self.parents = [0] * n
        self.min = [0] * n
        self.max = [0] * n
        self.count = [1] * n
        for i in range(n):
            self.parents[i] = i
            self.min[i] = i
            self.max[i] = i

    def print_snm(self):
        print(f'size: {self.n}')
        print(f'ranks: {self.rank}')
        print(f'parents: {self.parents}')
        print(f'min: {self.min}')
        print(f'max: {self.max}')
        print(f'count: {self.count}')

    def get(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.get(self.parents[x])

        return self.parents[x]

    def get_all(self, x):
        p = self.get(x)
        return self.min[p], self.max[p], self.count[p]

    def join(self, x, y):
        x = self.get(x)
        y = self.get(y)
        if x == y:
            return
        if self.rank[x] > self.rank[y]:
            x, y = y, x
        if self.rank[x] == self.rank[y]:
            self.rank[y] += 1

        self.parents[x] = y
        self.max[y] = max(self.max[x], self.max[y])
        self.min[y] = min(self.min[x], self.min[y])
        self.count[y] += self.count[x]

if __name__ == '__main__':
    data = sys.stdin.readlines()
    n = int(data[0])
    s = SNM(n)
    for line in data[1:]:
        if line[0] == 'u':
            x, y = map(int, line.split()[1:])
            s.join(x - 1, y - 1)
        else:
            mi, ma, co = s.get_all(int(line.split()[1]) - 1)
            print(mi + 1, ma + 1, co)