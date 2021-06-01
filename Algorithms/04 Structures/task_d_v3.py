"""Task D solution"""
import sys
import math

VERY_BIG_NUMBER = 10 ** 10

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

class Heap():
    def __init__(self):
        self.data = CircleArray()
        self.size = 0
        self.opp_count = 0
        
    def print_heap(self):
        """Prints heap. Just for debug"""
        n_rows = math.ceil(math.log2(self.size))
        offset = int(3 ** (n_rows - 1))
        row_start = 0
        row_end = 1
        for row in range(n_rows):
            print(' ' * offset, *self.data[row_start:row_end])
            offset = offset - 4
            row_start = row_end
            row_end += 2 ** (row + 1)
        #final line
        print(*self.data[row_start:self.size])
        
    def insert(self, value):
        """Inserts list (value, opp_num)"""
        self.opp_count += 1
        if self.size >= len(self.data):
            self.data.append([value, self.opp_count])
        else:
            self.data[self.size] = [value, self.opp_count]
        c_idx = self.size #Childs's position in data
        self.size += 1
        
        while c_idx > 0:
            p_idx = (c_idx - 1) // 2 #Parent's position in data
            if self.data[c_idx][0] >= self.data[p_idx][0]:
                break #early stoping
            else:
                self.data[c_idx], self.data[p_idx] = self.data[p_idx], self.data[c_idx]
            c_idx = p_idx
            
    def extract_min(self):
        """Extracts minimal element from heap and returns 2 values: value, n_opp"""
        self.opp_count += 1
        if self.size == 0:
            return VERY_BIG_NUMBER, -1
        
        result_val = self.data[0][0]
        result_pos = self.data[0][1]
        
        self.size -= 1
        self.data[0] =  self.data[self.size]
        
        idx_cur = 0
        while 2 * idx_cur + 1 < self.size:
            idx_left = 2 * idx_cur + 1
            idx_right = 2 * idx_cur + 2
            cur = self.data[idx_cur][0]
            left = self.data[idx_left][0]
            if idx_right == self.size:
                right = VERY_BIG_NUMBER
            else:
                right = self.data[idx_right][0]
                
            if left <= right and left < cur:
                self.data[idx_left], self.data[idx_cur] = self.data[idx_cur], self.data[idx_left]
                idx_cur = idx_left
            elif left >= right and right < cur:
                self.data[idx_right], self.data[idx_cur] = self.data[idx_cur], self.data[idx_right]
                idx_cur = idx_right
            else:
                break
                
        return result_val, result_pos
    
    def find_opp_position(self, opp_num):
        """returns position in data where operation opp_num resides. If not in heap - returns -1"""
        for idx, cur in enumerate(self.data):
            if cur[1] == opp_num:
                return idx
        return -1
    
    def decrease_key(self, key, value):
        """Changes value added at 'key' opp to 'value'"""
        self.opp_count += 1
        c_idx = self.find_opp_position(key) #Childs's position in data
        if c_idx < 0:
            return
        
        self.data[c_idx][0] = value
        while c_idx > 0:
            p_idx = (c_idx - 1) // 2 #Parent's position in data
            if self.data[c_idx][0] >= self.data[p_idx][0]:
                break #early stoping
            else:
                self.data[c_idx], self.data[p_idx] = self.data[p_idx], self.data[c_idx]
            c_idx = p_idx
            
if __name__ == '__main__':
    heap = Heap()
    for line in sys.stdin:
        if line[0] == 'p':
            heap.insert(int(line.split()[1]))
        elif line[0] == 'e':
            value, pos = heap.extract_min()
            if pos == -1:
                print('*')
            else:
                print(value, pos)
        elif line[0] == 'd':
            key, value = map(int, line.split()[1:])
            heap.decrease_key(key, value)
        elif line[0] == 'x':
            heap.print_heap()
