import sys 

class Node():
    def __init__(self, key):
        self.key = key
        self.h = 1
        self.nodes_count = 1 #Counter of nodes in tree below
        self.left = None
        self.right = None
        
    def print_node(self):
        print(self.key)
        
class AwlTree():
    def __init__(self):
        self.total_nodes = 0
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
    
    def nodes_count(self, node):
        if node == None:
            return 0
        else:
            return node.nodes_count
        
    def rotate_right(self, p):
        q = p.left
        p.left = q.right
        q.right = p
        q.nodes_count = self.nodes_count(q) + self.nodes_count(p.right) + 1
        p.nodes_count = self.nodes_count(p) - self.nodes_count(q.left) - 1
        self.fix_height(p)
        self.fix_height(q)
        return q
    
    def rotate_left(self, q):
        p = q.right
        q.right = p.left
        p.left = q
        q.nodes_count = self.nodes_count(q) - self.nodes_count(p.right) - 1
        p.nodes_count = self.nodes_count(p) + self.nodes_count(q.left) + 1
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
        tree.nodes_count += 1
        return self.balance(tree)
    
    def insert(self, k):
        self.total_nodes += 1
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
        
    def remove_min(self, node):
        if node == None:
            return None
        
        if node.left == None:
            return node.right
        node.left = self.remove_min(node.left)
        node.nodes_count -= 1
        return self.balance(node)
    
    def __remove(self, node, k):
        if node == None:
            return None
        
        if k < node.key:
            node.nodes_count -= 1
            node.left = self.__remove(node.left, k)
        elif k > node.key:
            node.nodes_count -= 1
            node.right = self.__remove(node.right, k)
        else:
            l = node.left
            r = node.right
            if r == None:
                return l
            new_root = self.find_min(r)
            new_root.right = self.remove_min(r)
            new_root.left = l
            new_root.nodes_count = self.nodes_count(new_root.left) \
                                    + self.nodes_count(new_root.right) + 1
            return self.balance(new_root)
        return self.balance(node)
        
    def remove(self, k):
        self.total_nodes -= 1
        self.root = self.__remove(self.root, k)
        
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
            print(shift, tree.key, tree.nodes_count)
            self.__print_tree(tree.right, shift + "  ")
            
    def print_tree(self):
        self.__print_tree(self.root)
        
    def nodes_to_left(self, node):
        if node == None:
            return 0
        return self.nodes_count(node) - self.nodes_count(node.right)
    
    def __find_kth(self, node, to_go):
        collected = self.nodes_to_left(node)
        if collected - to_go == 1:
            return node
        
        if collected - to_go < 1:
            return self.__find_kth(node.right, to_go - collected)
        else:
            return self.__find_kth(node.left, to_go)
        
    def find_kth(self, k):
        return self.__find_kth(self.root, self.total_nodes - k).key
    
if __name__ == '__main__':
    tree = AwlTree()
    data = sys.stdin.readlines()
    res = []
    for line in data[1:]:
        if line[0] == '1' or line[0] == '+':
            tree.insert(int(line.split()[1]))
        elif line[0] == '-':
            tree.remove(int(line.split()[1]))
        elif line[0] == '0':
            res.append(str(tree.find_kth(int(line.split()[1]))))
            
    sys.stdout.write('\n'.join(res))