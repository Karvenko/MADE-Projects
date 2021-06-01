"""Task A solution"""

import sys

VERY_BIG_NUMBER = 10 ** 11 #Constant to find minimum

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList():
    def __init__(self):
        self.start = None
        self.len = 0
        
    def push(self, value):
        """Adds element to the beginning of list"""
        new_node = Node(value)
        new_node.next = self.start
        self.start = new_node
        self.len += 1
        
    def pop(self):
        """Removes element from the beginning and returns it's value"""
        result = self.start.value
        self.start = self.start.next
        self.len -= 1
        return result
    
    def print_list(self):
        """Prints list - for debug"""
        cur = self.start
        
        while cur != None:
            print(cur.value)
            cur = cur.next
            
class Stack():
    def __init__(self):
        self.data = LinkedList()
        self.min = VERY_BIG_NUMBER
        
    def push(self, value):
        """Pushes tuple (value, previous_min) to array"""
        if value <= self.min:
            prev_min = self.min
            self.min = value
            self.data.push((value, prev_min))
        else:
            self.data.push((value, VERY_BIG_NUMBER))
            
    def pop(self):
        """Pops element from stack. Updates minimum if nessesary"""
        result = self.data.pop()
        if result[0] == self.min: #Removing smallest element
            self.min = result[1]
            
        return result[0]
    
    def get_minimum(self):
        assert self.data.len > 0
        return self.min
    

if __name__ == '__main__':
    stack = Stack()
    
    n_requests = int(sys.stdin.readline())
    for _ in range(n_requests):
        cur_req = sys.stdin.readline()
        if cur_req[0] == '1': #Push
            stack.push(int(cur_req.split()[1]))
        elif cur_req[0] == '2': ##Pop
            _ = stack.pop()
        else:
            sys.stdout.write(str(stack.get_minimum()) + '\n')
            
