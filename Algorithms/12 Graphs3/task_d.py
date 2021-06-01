"""Task D solution"""
import sys

class SNM:
    def __init__(self, n):
        self.n = n
        self.rank = [0] * n
        self.parents = [0] * n

        for i in range(n):
            self.parents[i] = i

    def print_snm(self):
        print(f'size: {self.n}')
        print(f'ranks: {self.rank}')
        print(f'parents: {self.parents}')

    def get(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.get(self.parents[x])
        return self.parents[x]


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

def find_mst(arr, n):
    arr = sorted(arr)
    s = SNM(n)
    total = 0
    for i in range(len(arr)):
        if s.get(arr[i][1]) != s.get(arr[i][2]):
            s.join(arr[i][1], arr[i][2])
            total += arr[i][0]
    return total

if __name__ == '__main__':
    data = sys.stdin.readlines()
    n, m = map(int, data[0].split())
    arr = []
    for line in data[1:]:
        f, t, w = map(int, line.split())
        arr.append([w, f - 1, t - 1])
    print(find_mst(arr, n))