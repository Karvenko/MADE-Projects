from collections import defaultdict, deque
import sys

SHIFTS = [[2, 1], [2, -1], [-2, 1], [-2, -1],
          [1, 2], [1, -2], [-1, 2], [-1, -2]]
DEFAULT_COLOR = 0
NODE_VISITED = 1
COLOR_BLACK = 1
COLOR_GRAY = 2
COLOR_USED = 10
NO_WAY = -1

def add_shift(point, shift):
    return [point[0] + shift[0], point[1] + shift[1]]

def get_neighbours(point):
    return [add_shift(point, shift) for shift in SHIFTS]


class Node:
    def __init__(self, name: int, color=DEFAULT_COLOR):
        self.name = name
        self.color = color
        self.edges = []

    def add_edge(self, neighbour):
        self.edges.append(neighbour)

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def print_node(self):
        print(f'id: {self.name} color: {self.color}: {self.edges}')

class Graph:
    def __init__(self, n_nodes=None, oriented=False):
        self.n_conn = None
        self.nodes = defaultdict()
        self.oriented = oriented
        self.n_nodes = n_nodes
        if n_nodes:
            for i in range(n_nodes):
                self.nodes[i] = Node(i)

    def add_node(self, node_id):
        if node_id not in self.nodes.keys():
            self.nodes[node_id] = Node(node_id)

    def init_from_array(self, edge_array):
        for edge in edge_array:
            self.add_node(edge[0])
            self.add_node(edge[1])
            self.nodes[edge[0]].add_edge(edge[1])

        if not self.oriented:
            for edge in edge_array:
                self.nodes[edge[1]].add_edge(edge[0])

    def add_edge(self, start, end):
        # print('jjjj', start, end)
        self.nodes[start].add_edge(end)
        if not self.oriented:
            self.nodes[end].add_edge(start)

    def print_graph(self):
        for node in self.nodes.values():
            node.print_node()

    def bfs_search(self, start):
        distance = [NO_WAY] * self.n_nodes
        parents = [NO_WAY] * self.n_nodes
        qu = deque()

        distance[start] = 0
        qu.append(start)
        self.nodes[start].set_color(COLOR_USED)

        while len(qu) > 0:
            v = qu.popleft()
            # print(qu)
            for u in self.nodes[v].edges:
                if self.nodes[u].get_color() != COLOR_USED:
                    self.nodes[u].set_color(COLOR_USED)
                    distance[u] = distance[v] + 1
                    parents[u] = v
                    qu.append(u)

        # print(distance)
        # print(parents)
        return distance, parents

class ChessField:
    def __init__(self, size):
        self.size = size
        self.gr = Graph(self.size ** 2, oriented=True)
        for i in range(self.size):
            for j in range(self.size):
                edges = get_neighbours([i, j])
                for edge in edges:
                    if self.is_correct_point(edge):
                        # print(edge)
                        self.gr.add_edge(self.point_to_num([i, j]),
                                         self.point_to_num(edge))

    def point_to_num(self, point):
        return point[0] * self.size + point[1]

    def num_to_point(self, n):
        return [n // self.size, n % self.size]

    def is_correct_point(self, point):
        return point[0] >= 0 and point[1] >= 0 and \
               point[0] < self.size and point[1] < self.size

    def find_way(self, start_point, end_point):
        start = self.point_to_num(start_point)
        end = self.point_to_num(end_point)
        distance, parents = self.gr.bfs_search(start)
        way = []
        cur = end
        while cur != start:
            way.append(self.num_to_point(cur))
            cur = parents[cur]
        way.append(start_point)
        return list(reversed(way))

if __name__ == '__main__':
    data = sys.stdin.readlines()
    arr = []
    for line in data:
        line = line.split()
        for num in line:
            arr.append(int(num))

    cf = ChessField(arr[0])
    result = cf.find_way([arr[1] - 1, arr[2] - 1],
                         [arr[3] - 1, arr[4] - 1])
    print(len(result))
    for point in result:
        print(point[0] + 1, point[1] + 1)