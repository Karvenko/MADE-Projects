"""Task C solution"""

class CircleArray():
    """Self-expanding circle array"""
    def __init__(self, init_capacity=2):
        self.data = [None] * init_capacity
        self.capacity = init_capacity
        self.len = 0
        self.start = 0
        
    def __getitem__(self, key):
        """Redefined [] operator"""
        return self.data[(self.start + key) % self.capacity]
    
    def __setitem__(self, key, value):
        """Redefined [] =  operator"""
        self.data[(self.start + key) % self.capacity] = value
        
    def __len__(self):
        return self.len
        
    def expand_array(self):
        """Expands array in two times"""
        new_capacity = self.capacity * 2
        self.resize_array(new_capacity)
        
    def shrink_array(self):
        """Shrinks array in two times"""
        new_capacity = self.capacity // 2
        self.resize_array(new_capacity)
        
    def resize_array(self, new_capacity):
        """Sets new capacity of array"""
        new_data = [None] * new_capacity
        for idx in range(self.len):
            new_data[idx] = self.data[(self.start + idx) % self.capacity]
        #reseting indexes    
        self.start = 0
        self.data = new_data
        self.capacity = new_capacity
        
    def append(self, value):  
        """Appends item at the end of array"""
        self.data[(self.start + self.len) % self.capacity] = value
        self.len += 1
        if self.len ==  self.capacity:
            self.expand_array()
        
    def last(self):
        """Returns last element of array"""
        return self.data[(self.start + self.len - 1) % self.capacity]
    
    def pop(self):
        """Returns last element of arrasy and removes it"""
        result = self.data[(self.start + self.len - 1) % self.capacity]
        self.len -= 1
        if self.len * 4 <= self.capacity:
            self.shrink_array()
        return result
            
    def first(self):
        """Returns first element"""
        return self.data[self.start]
    
    def delete_first(self):
        """Returns first element of array and deletes it"""
        result = self.data[self.start]
        self.start = (self.start + 1) % self.capacity
        self.len -= 1
        if self.len * 4 <= self.capacity:
            self.shrink_array()
        return result
    
class Queue():
    """Queue class"""
    def __init__(self):
        self.data = CircleArray()
        
    def add(self, value):
        """Adds element to queue"""
        self.data.append(value)
        
    def remove(self):
        """Remove element from queue"""
        return self.data.delete_first()
    
def proceed_request(queue, request):
    """Procceds request for queue"""
    if request[0] == '-':
        return queue.remove()
    else:
        queue.add(int(request.split()[1]))
        return None
    
if __name__ == '__main__':
    queue = Queue()
    n_req = int(input())
    for _ in range(n_req):
        result = proceed_request(queue, input())
        if result:
            print(result)
