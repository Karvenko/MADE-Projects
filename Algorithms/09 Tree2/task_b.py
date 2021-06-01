"""Task B solution"""

from random import randint
import sys

RAND_MAX = 10 ** 10

class Node():
    def __init__(self, value):
        self.sum = 1
        self.y = randint(0, RAND_MAX)
        self.value = value
        self.left = None
        self.right = None
        
    def print_node(self):
        print(self.key)
        
class Treap():
    def __init__(self):
        self.root = None
        
    def count(self, node):
        if node != None:
            return node.sum
        else:
            return 0
    
    def fix_sum(self, node):
        if not node:
            return
        node.sum = self.count(node.left) + self.count(node.right) + 1
        
    def __split(self, node, x):
        if node == None:
            return None, None
        if node.sum - self.count(node.right) > x:
            t1, t2 = self.__split(node.left, x)
            node.left = t2
            self.fix_sum(node)
            return t1, node
        else:
            t1, t2 = self.__split(node.right, x - self.count(node.left) - 1)
            node.right = t1
            self.fix_sum(node)
            return node, t2
        
    def split(self, x):
        return self.__split(self.root, x)
    
    def merge(self, t1, t2):
        if t1 == None:
            return t2
        if t2 == None:
            return t1
        
        if t1.y > t2.y:
            t1.right = self.merge(t1.right, t2)
            self.fix_sum(t1)
            return t1
        else:
            t2.left = self.merge(t1, t2.left)
            self.fix_sum(t2)
            return t2
        
    def insert(self, idx, key):
        t1, t2 = self.split(idx)
        tmp = self.merge(t1, Node(key))
        self.root = self.merge(tmp, t2)
            
    def remove(self, idx):
        t1, t2 = self.split(idx)
        t11, _ = self.__split(t1, idx - 1)
        self.root = self.merge(t11, t2)
    
    def find_min(self, node):
        if node == None:
            return None
        if node.left != None:
            return self.find_min(node.left)
        else:
            return node
        
    def find_max(self, node):
        if node == None:
            return None
        if node.right != None:
            return self.find_max(node.right)
        else:
            return node
        
    def __search(self, node, k):
        if node == None:
            return False
        if k < node.x:
            return self.__search(node.left, k)
        elif k > node.x:
            return self.__search(node.right, k)
        else:
            return True
                
    def search(self, k):
        return self.__search(self.root, k)
    
    def find_next(self, key, tree=None):
        if tree == None:
            pointer = self.root
        else:
            pointer = tree

        result = None
        while pointer != None:
            if key < pointer.x:
                result = pointer
                pointer = pointer.left
            else:
                pointer = pointer.right
        return result
    
    def find_prev(self, key, tree=None):
        if tree == None:
            pointer = self.root
        else:
            pointer = tree
            
        result = None
        while pointer != None:
            if key > pointer.x:
                result = pointer
                pointer = pointer.right
            else:
                pointer = pointer.left
        return result
    
    def __print_tree(self, tree, shift=""):
        if tree != None:
            self.__print_tree(tree.right, shift + "  ")
            print(shift, tree.value, tree.sum)
            self.__print_tree(tree.left, shift + "  ")
            
    def print_tree(self):
        self.__print_tree(self.root)
        
    def __return_tree(self, tree):
        if tree == None:
            return []
        result = []
        result.extend(self.__return_tree(tree.left))
        result.append(tree.value)
        result.extend(self.__return_tree(tree.right))
        return result
        
    def return_tree(self):
        return self.__return_tree(self.root)
    
    def fill_tree(self, values):
        for i in range(len(values) - 1, -1, -1):
            self.insert(0, values[i])
            
if __name__ == '__main__':
    tree = Treap()
    data = sys.stdin.readlines()
    n, m = map(int, data[0].split())
    array = [int(x) for x in data[1].split()]
    tree.fill_tree(array)
    
    for line in data[2:]:
        if line[0] == 'a':
            idx, val = map(int, line.split()[1:])
            tree.insert(idx, val)
        elif line[0] == 'd':
            tree.remove(int(line.split()[1]))
            
    result = tree.return_tree()
    print(len(result))
    print(*result)
    
