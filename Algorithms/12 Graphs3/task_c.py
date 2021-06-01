"""Task C solution"""
import sys

INF = 10 ** 20

def dist(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

class Graph:
    def __init__(self, array):
        self.n_nodes = len(array)
        self.nodes = array
        self.used = [False] * self.n_nodes
        self.min_l = [INF] * self.n_nodes
        # self.closest = [-1] * self.n_nodes

    def find_mst(self):
        self.min_l[0] = 0
        for _ in range(self.n_nodes):
            next = -1
            for i in range(self.n_nodes):
                if not self.used[i] and (next == -1 or self.min_l[i] < self.min_l[next]):
                    next = i

            self.used[next] = True
            for i in range(self.n_nodes):
                # cur_dist = dist(self.nodes[next], self.nodes[i])
                if i != next and not self.used[i]:
                    cur_dist = dist(self.nodes[next], self.nodes[i])
                    if cur_dist < self.min_l[i]:
                        self.min_l[i] = cur_dist
                    # self.closest[i] = next
        # return self.min_l, self.closest
        return sum(self.min_l)

if __name__ == '__main__':
    data = sys.stdin.readlines()
    array = []
    for line in data[1:]:
        x, y = map(int, line.split())
        array.append((x, y))
    g = Graph(array)
    print(g.find_mst())