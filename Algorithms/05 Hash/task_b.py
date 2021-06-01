"""Task B solution"""

import random
import sys

PRIMES_SMALL = [31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
PRIMES_BIG = [1000589, 1000609, 1000619, 1000621, 1000639, 1000651, 1000667, 1000669, 1000679, 1000691]

class Hasher():
    def __init__(self, arr_size):
        self.arr_size = arr_size
        self.a = random.sample(PRIMES_SMALL, 1)[0]
        self.p = random.sample(PRIMES_BIG, 1)[0]
        
    def get_int_hash(self, value):
        """Returns hash for int"""
        return ((self.a * value) % self.p) % self.arr_size
    
    def get_str_hash(self, string):
        """Returns hash for string"""
        result = 0
        for ch in string:
            result = (result * self.a + ord(ch)) % self.p
            
        result %= self.arr_size
        return result
    
    def get_hash(self, value):
        """Returns hash for in or string"""
        if type(value) == int:
            return self.get_int_hash(value)
        else:
            return self.get_str_hash(value)

class Node():
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self):
        self.data = None
        self.size = 0
        
    def add(self, key, value):
        """Adds element to linked list, returns True if new element and False otherwise"""
        pointer = self.data
        
        while pointer != None:
            if pointer.key == key:
                pointer.value = value
                return False
            pointer = pointer.next
            
        if pointer == None:
            new_node = Node(key, value)
            new_node.next = self.data
            self.data = new_node
            self.size += 1
        return True
    
    def get(self, key):
        """Get value by key"""
        if self.size == 0:
            return None
        
        pointer = self.data
        
        while pointer != None:
            if pointer.key == key:
                return pointer.value
            pointer = pointer.next
            
        return None
    
    def delete(self, key):
        """Deletes element key from list. Returns True if element was deleted and False otherwise"""
        if self.size == 0:
            return False
        
        if self.data.key == key:
            self.data = self.data.next
            self.size -= 1
            return True
            
        prev_pointer = self.data
        cur_pointer = self.data.next
        while cur_pointer != None:
            if cur_pointer.key == key:
                prev_pointer.next = cur_pointer.next
                self.size -= 1
                return True
            prev_pointer = cur_pointer
            cur_pointer = cur_pointer.next
        return False
            
    def top(self):
        """Returns key & value for first element"""
        if self.size == 0:
            return None, None
        else:
            return self.data.key, self.data.value
            
    def print_list(self):
        """Printing - just for debug"""
        cur = self.data
        while cur != None:
            print('(', cur.key, cur.value, ')')
            cur = cur.next

class HashMap():
    def __init__(self, init_size=4):
        self.capacity = init_size
        self.size = 0
        self.hasher = Hasher(self.capacity)
        self.data = [LinkedList() for i in range(self.capacity)]
        
        
    def add(self, key, value):
        """Adds key, value to map"""
        idx = self.hasher.get_hash(key)
        res = self.data[idx].add(key, value)
        if res:
            self.size += 1
            if self.size * 2 > self.capacity:
                self.expand_map()
        
    def print_map(self):
        """Prints Hash Map - just for debug"""
        for i in range(len(self.data)):
            print('List: ', i)
            self.data[i].print_list()
            print('\n')
            
    def delete(self, key):
        """Deletes key from map"""
        idx = self.hasher.get_hash(key)
        res = self.data[idx].delete(key)
        if res:
            self.size -= 1
            if self.size * 4 < self.capacity:
                self.shrink_map()
        
    def get(self, key):
        """GEts key value from map"""
        idx = self.hasher.get_hash(key)
        return(self.data[idx].get(key))
    
    def resize(self, new_cap):
        """Resize hash map"""
        new_data = [LinkedList() for i in range(new_cap)]
        self.hasher = Hasher(new_cap)
        for cur in self.data:
            for _ in range(cur.size):
                key, value = cur.top()
                idx = self.hasher.get_hash(key)
                new_data[idx].add(key, value)
                cur.delete(key)
        self.data = new_data
        self.capacity = new_cap
        
    def expand_map(self):
        """Doubles capacity"""
        self.resize(self.capacity * 2)
        
    def shrink_map(self):
        """decrease capacity 2 times"""
        self.resize(self.capacity // 2)
        

if __name__ == '__main__':
    hashmap = HashMap()
    for line in sys.stdin:
        if line[0] == 'p':
            key, value = line.split()[1:]
            hashmap.add(key, value)
        elif line[0] == 'd':
            hashmap.delete(line.split()[1])
        elif line[0] == 'g':
            res = hashmap.get(line.split()[1])
            if res != None:
                print(res)
            else:
                print('none')
