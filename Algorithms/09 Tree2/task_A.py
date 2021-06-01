"""Task A solution"""

import sys
from random import randint

RAND_MAX = 10 ** 10

class Node():
    def __init__(self, x):
        self.x = x
        self.y = randint(0, RAND_MAX)
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
        
    def __split(self, node, x):
        if node == None:
            return None, None
        if node.x > x:
            t1, t2 = self.__split(node.left, x)
            node.left = t2
            return t1, node
        else:
            t1, t2 = self.__split(node.right, x)
            node.right = t1
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
            return t1
        else:
            t2.left = self.merge(t1, t2.left)
            return t2
        
    def insert(self, x):
        if self.search(x) == False:
            t1, t2 = self.split(x)
            tmp = self.merge(t1, Node(x))
            self.root = self.merge(tmp, t2)
            
    def remove(self, x):
        if self.search(x) == True:
            t1, t2 = self.split(x)
            t11, _ = self.__split(t1, x - 1)
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
            print(shift, tree.x)
            self.__print_tree(tree.left, shift + "  ")
            
    def print_tree(self):
        self.__print_tree(self.root)
        

if __name__ == '__main__':
    tree = Treap()
    data = sys.stdin.readlines()
    for line in data:
        if line[0] == 'i':
            _ = tree.insert(int(line.split()[1]))
        elif line[0] == 'd':
            _ = tree.remove(int(line.split()[1]))
        elif line[0] == 'e':
            res = tree.search(int(line.split()[1]))
            if res == False:
                print('false')
            else:
                print('true')
        elif line[0] == 'n':
            res = tree.find_next(int(line.split()[1]))
            if res != None:
                print(res.x)
            else:
                print('none')
        elif line[0] == 'p':
            res = tree.find_prev(int(line.split()[1]))
            if res != None:
                print(res.x)
            else:
                print('none')
            