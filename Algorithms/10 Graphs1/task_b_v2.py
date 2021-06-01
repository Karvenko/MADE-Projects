"""Task B - deep search with DFS"""
from collections import defaultdict
import sys
from sys import setrecursionlimit
import threading

DEFAULT_COLOR = 0
NODE_VISITED = 1

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
    def __init__(self, n_nodes=None, oriented=False):
        self.n_conn = None
        self.nodes = defaultdict()
        self.oriented = oriented
        if n_nodes:
            for i in range(n_nodes):
                self.nodes[i] = Node(i)


    def add_node(self, node_id):
        if node_id not in self.nodes.keys():
            self.nodes[node_id] = Node(node_id)


    def init_from_array(self, edge_array):
#         print(edge_array)

        for edge in edge_array:
            self.add_node(edge[0])
            self.add_node(edge[1])
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

    def dfs_depth_search(self, node_id):
        self.nodes[node_id].set_color(NODE_VISITED)
        max_depth = 0
        for child_name in self.nodes[node_id].edges:
            if self.nodes[child_name].color == DEFAULT_COLOR:
                tmp = self.dfs_depth_search(child_name)
                if tmp > max_depth:
                    max_depth = tmp
        return max_depth + 1
                
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
    n = int(data[0])
    edges = []
    for edge in data[1:]:
        e, _, b = edge.lower().split()
        edges.append([b, e])

    graph = Graph()
    graph.init_from_array(edges)
    print(graph.dfs_depth_search('polycarp'))
    return
        
if __name__ == '__main__':    
    setrecursionlimit(10 ** 9)
    threading.stack_size(2 ** 26)  # лучше использовать именно эту константу
    thread = threading.Thread(target=main)
    thread.start()
    thread.join()