"""Task D solution"""

import sys

MOD_9 = 10 ** 9

class Node():
    def __init__(self, key):
        self.key = key
        self.h = 1
        self.sum = key #sum of all elements in tree
        self.left = None
        self.right = None
        
    def print_node(self):
        print(self.key)
        
class AwlTree():
    def __init__(self):
        self.root = None
        
    def height(self, node):
        if node != None:
            return node.h
        else:
            return 0
    
    def bal_factor(self, node):
        if node != None:
            return self.height(node.right) - self.height(node.left)
        else:
            return 0
        
    def fix_height(self, node):
        node.h = max(self.height(node.right), self.height(node.left)) + 1
        return
    
    def get_sum(self, node):
        if node == None:
            return 0
        else:
            return node.sum
        
    def get_left_sum(self, node):
        if node == None:
            return 0
        else:
            return node.sum - self.get_sum(node.right)
    
    def rotate_right(self, p):
        q = p.left
        p.left = q.right
        q.right = p
        p.sum = self.get_sum(p.right) + self.get_sum(p.left) + p.key
        q.sum = self.get_sum(q.left) + q.key + self.get_sum(p)
        self.fix_height(p)
        self.fix_height(q)
        return q
    
    def rotate_left(self, q):
        p = q.right
        q.right = p.left
        p.left = q
        q.sum = self.get_sum(q.left) + self.get_sum(q.right) + q.key
        p.sum = self.get_sum(q) + self.get_sum(p.right) + p.key
        self.fix_height(q)
        self.fix_height(p)
        return p
    
    def balance(self, node):
        self.fix_height(node)
        if self.bal_factor(node) == 2:
            if self.bal_factor(node.right) < 0:
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        elif self.bal_factor(node) == -2:
            if self.bal_factor(node.left) > 0:
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        else:
            return node
        
    def __insert(self, tree, k):
        if tree == None:
            return Node(k)
        
        if k < tree.key:
            tree.left = self.__insert(tree.left, k)
        elif k > tree.key:
            tree.right = self.__insert(tree.right, k)
        tree.sum += k
        
        return self.balance(tree)
    
    def insert(self, k):
        if not self.search(k):
            self.root = self.__insert(self.root, k)
        
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
        if k < node.key:
            return self.__search(node.left, k)
        elif k > node.key:
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
            if key < pointer.key:
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
            if key > pointer.key:
                result = pointer
                pointer = pointer.right
            else:
                pointer = pointer.left
        return result
    
    def __print_tree(self, tree, shift=""):
        if tree != None:
            self.__print_tree(tree.left, shift + "  ")
            print(shift, tree.key, tree.sum)
            self.__print_tree(tree.right, shift + "  ")
            
    def print_tree(self):
        self.__print_tree(self.root)
        
    def __count_left_sum(self, node, key):
        if node == None:
            return 0
        if key == node.key:
            return self.get_left_sum(node) - node.key
        
        if key < node.key:
            return self.__count_left_sum(node.left, key)
        else:
            return self.get_left_sum(node) + self.__count_left_sum(node.right, key)
        
    def count_left_sum(self, key):
        return self.__count_left_sum(self.root, key)
    
    def find_sum(self, left, right):
        return self.count_left_sum(right + 1) - self.count_left_sum(left) 
    
if __name__ == '__main__':
    tree = AwlTree()
    data = sys.stdin.readlines()
    need_add = False
    prev = 0
    res = []
    
    for line in data[1:]:
        if line[0] == '+':
            x = int(line.split()[1])
            if need_add:
                x = (x + prev) % MOD_9
                need_add = False
            tree.insert(x)
        elif line[0] == '?':
            prev = tree.find_sum(int(line.split()[1]), int(line.split()[2]))
            need_add = True
            res.append(str(prev))
            
    sys.stdout.write('\n'.join(res))
    