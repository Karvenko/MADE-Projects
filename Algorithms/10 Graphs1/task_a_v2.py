from collections import defaultdict
import sys
from sys import setrecursionlimit
import threading

DEFAULT_COLOR = 0

class Node():
    def __init__(self, name: int, color=DEFAULT_COLOR):
        self.name = name
        self.color = color
        self.edges = []


    def add_edge(self, neighboor):
        self.edges.append(neighboor)


    def get_color(self):
        return self.color


    def set_color(self, color):
        self.color = color

    def print_node(self):
        print(f'id: {self.name} color: {self.color}: {self.edges}')
        
class Graph():
    def __init__(self, n_nodes, oriented=False):
        self.n_conn = None
        self.nodes = defaultdict()
        self.oriented = oriented
        for i in range(n_nodes):
            self.nodes[i] = Node(i)


    def init_from_array(self, edge_array):
#         print(edge_array)
        for edge in edge_array:
            self.nodes[edge[0]].add_edge(edge[1])

        if not self.oriented:
            for edge in edge_array:
                self.nodes[edge[1]].add_edge(edge[0])


    def print_graph(self):
        for node in self.nodes.values():
            node.print_node()
            
    def dfs_color_graph(self, node_id, color):
        self.nodes[node_id].set_color(color)
        for child_idx in self.nodes[node_id].edges:
            if self.nodes[child_idx].get_color() == DEFAULT_COLOR:
                self.dfs_color_graph(child_idx, color)
                
    def find_connectivity(self):
        self.n_conn = 0
        for node in self.nodes.values():
            if node.get_color() == DEFAULT_COLOR:
                self.n_conn += 1
                self.dfs_color_graph(node.name, self.n_conn)
                
    def print_connectivity(self):
        print(self.n_conn)
        res = []
        for node in self.nodes.values():
            res.append(str(node.color))
        print(' '.join(res))
        
def main():
    data = sys.stdin.readlines()
    n, m = map(int, data[0].split())
    edges = []
    for edge in range(1, m + 1):
        b, e = map(int, data[edge].split())
        edges.append([b - 1, e - 1])
        
    graph = Graph(n)
    graph.init_from_array(edges)
    graph.find_connectivity()
    graph.print_connectivity()
    return
        
if __name__ == '__main__':    
    setrecursionlimit(10 ** 9)
    threading.stack_size(2 ** 26)  # лучше использовать именно эту константу
    thread = threading.Thread(target=main)
    thread.start()
    thread.join()