from collections import defaultdict, deque
import sys
import heapq

DEFAULT_COLOR = 0
NODE_VISITED = 1
COLOR_BLACK = 1
COLOR_GRAY = 2
COLOR_USED = 10
NO_SHORTEST_WAY = -10 ** 20
INF = 10 ** 20



class Node:
    def __init__(self, name: int):
        self.name = name
        # self.color = color
        self.edges = []

    def add_edge(self, neighbour):
        self.edges.append(neighbour)

    # def get_color(self):
    #     return self.color
    #
    # def set_color(self, color):
    #     self.color = color

    def print_node(self):
        print(f'id: {self.name}: {self.edges}')

class Graph:
    def __init__(self, n_nodes=None, oriented=False):
        self.n_conn = None
        # self.nodes = defaultdict()
        self.nodes = []
        self.oriented = oriented
        self.n_nodes = n_nodes
        if n_nodes:
            for i in range(n_nodes):
                self.nodes.append(Node(i))

    # def add_node(self, node_id):
    #     if node_id not in self.nodes.keys():
    #         self.nodes[node_id] = Node(node_id)

    def init_from_array(self, edge_array):
        """Init from array for weighted graph"""
        for edge in edge_array:
            # self.add_node(edge[0])
            # self.add_node(edge[1])
            self.nodes[edge[0]].add_edge([edge[1], edge[2]])

        if not self.oriented:
            for edge in edge_array:
                self.nodes[edge[1]].add_edge([edge[0], edge[2]])

    def add_edge(self, start, end):
        # print('jjjj', start, end)
        self.nodes[start].add_edge(end)
        if not self.oriented:
            self.nodes[end].add_edge(start)

    def print_graph(self):
        for node in self.nodes:
            node.print_node()

    def dijkstra(self, start):
        distance = [INF] * self.n_nodes
        used = [False] * self.n_nodes
        q = []
        heapq.heappush(q, [0, start])
        distance[start] = 0
        for _ in range(self.n_nodes):
            if len(q) == 0:
                break
            was_used = True
            while was_used:
                next = heapq.heappop(q)[1]
                was_used = used[next]
            used[next] = True
            for edge in self.nodes[next].edges:
                distance[edge[0]] = min(distance[edge[0]], distance[next] + edge[1])
                heapq.heappush(q, [distance[edge[0]], edge[0]])
        return distance

    def make_fb_step(self, distances):
        new_dist = [INF] * self.n_nodes
        for idx, node in enumerate(self.nodes):
            for edge in node.edges:
                new_dist[idx] = min(distances[idx], distances[edge[0]] + edge[1])
        return new_dist

    def ford_bellman(self, start):
        distances = [INF] * self.n_nodes
        distances[start] = 0
        for _ in range(self.n_nodes - 1):
            distances = self.make_fb_step(distances)

        check_dist = self.make_fb_step(distances)
        for idx in len(distances):
            if check_dist[idx] < distances[idx]:
                distances[idx] = NO_SHORTEST_WAY
        return distances

if __name__ == '__main__':
    data = sys.stdin.readlines()
    n, m, s= map(int, data[0].split())
    arr = []
    for line in data[1:]:
        a, b, c = map(int, line.split())
        arr.append([a - 1, b - 1, c])

    gr = Graph(n, oriented=True)
    gr.init_from_array(arr)
    # gr.print_graph()
    result = gr.ford_bellman(s)
    for cur in result:
        if cur >= INF:
            print('*')
        elif cur <= NO_SHORTEST_WAY:
            print('-')
        else:
            print(cur)