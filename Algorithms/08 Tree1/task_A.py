"""Task A solution"""

import sys

class Node():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        
    def print_node(self):
        print(self.key)
        
class MyTree():
    def __init__(self):
        self.root = None
        
    def __insert(self, key, tree):
        if tree == None:
            return Node(key)
        if key < tree.key:
            tree.left = self.__insert(key, tree.left)
            return tree
        elif key > tree.key:
            tree.right = self.__insert(key, tree.right)
            return tree
        else:
            return tree
        
    def __print_tree(self, tree):
        if tree != None:
            self.__print_tree(tree.left)
            print(tree.key, ' ')
            self.__print_tree(tree.right)
            
    def insert(self, key):
        self.root = self.__insert(key, self.root)
        
    def search(self, key, tree=None):
        if tree == None:
            pointer = self.root
        else:
            pointer = tree
        while pointer != None:
            if pointer.key == key:
                return pointer
            elif key < pointer.key:
                pointer = pointer.left
            else:
                pointer = pointer.right
        return None
    
    def find_smallest(self, tree=None):
        if tree == None:
            pointer = self.root
        else:
            pointer = tree
            
        if pointer.left == None:
            return None
        
        while pointer.left != None:
            pointer = pointer.left
        return pointer
    
    def find_biggest(self, tree=None):
        if tree == None:
            pointer = self.root
        else:
            pointer = tree
            
        if pointer.right == None:
            return pointer
        
        while pointer.right != None:
            pointer = pointer.right
        return pointer
    
    def __delete(self, key, tree=None):
        prev_node = None
        if tree == None:
            tree_start = self.root
            pointer = self.root
        else:
            tree_start = tree
            pointer = tree
            
        if pointer == None:
            return None
        
        while pointer != None:
            if key < pointer.key:
                prev_node = pointer
                pointer = pointer.left
            elif key > pointer.key:
                prev_node = pointer
                pointer = pointer.right
            else: #key found
                break
                
        if pointer == None:
            return tree_start
        
        if prev_node == None:
            if pointer.left == None: 
                return pointer.right
            elif pointer.right == None:
                return pointer.left
                
        if pointer.left == None and pointer.right == None:
            if key < prev_node.key:
                prev_node.left = None
            else:
                prev_node.right = None
        elif pointer.left == None:
            if key < prev_node.key:
                prev_node.left = pointer.right
            else:
                prev_node.right = pointer.right
        elif pointer.right == None:
            if key < prev_node.key:
                prev_node.left = pointer.left
            else:
                prev_node.right = pointer.left
        else:
            res = self.find_biggest(tree=pointer.left)
            pointer.key = res.key
            pointer.left = self.__delete(res.key, tree=pointer.left)
            
        return tree_start
    
    def delete(self, key):
        self.root = self.__delete(key)
    
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
            
    def print_tree(self):
        self.__print_tree(self.root)
        
if __name__ == '__main__':
    tree = MyTree()
    data = sys.stdin.readlines()
    for line in data:
        if line[0] == 'i':
            _ = tree.insert(int(line.split()[1]))
        elif line[0] == 'd':
            _ = tree.delete(int(line.split()[1]))
        elif line[0] == 'e':
            res = tree.search(int(line.split()[1]))
            if res == None:
                print('false')
            else:
                print('true')
        elif line[0] == 'n':
            res = tree.find_next(int(line.split()[1]))
            if res != None:
                print(res.key)
            else:
                print('none')
        elif line[0] == 'p':
            res = tree.find_prev(int(line.split()[1]))
            if res != None:
                print(res.key)
            else:
                print('none')
            