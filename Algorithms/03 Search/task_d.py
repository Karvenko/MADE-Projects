"""TAsk D solution"""

MIN_LENGTH = 1
MAX_LENGTH = 10000001

class Camp:
    def __init__(self, n_houses, rope_array):
        self.rope_array = rope_array
        self.n_houses = n_houses
        
    def house_number(self, rope_len):
        """Count number of houses if use rope_len as rope length"""
        len_sum = 0
        
        for rope in self.rope_array:
            len_sum += rope // rope_len
            
        return len_sum
    
    def can_fill(self, rope_len):
        """Returns true if we can fill all houses with ropes of rope_len"""
        return (self.n_houses <= self.house_number(rope_len))
    

def find_int_root(func, low, high):
    """find integer root for decreasing boolean function func"""
    if func(low) <= 0:
        return 0
    tmp_low = low
    tmp_high = high
    middle = (tmp_high - tmp_low) // 2 + tmp_low
    
    while tmp_high - tmp_low > 2:
        if func(middle):
            tmp_low = middle
        else:
            tmp_high = middle
            
        middle = (tmp_high - tmp_low) // 2 + tmp_low
    
    if func(middle):
        return middle
    else:
        return tmp_low
    

if __name__ == '__main__':
    n_ropes, n_houses = map(int, input().split())
    
    rope_array = [0] * n_ropes
    for i in range(n_ropes):
        rope_array[i] = int(input())
        
    camp = Camp(n_houses, rope_array)
    print(find_int_root(camp.can_fill, MIN_LENGTH, MAX_LENGTH))
