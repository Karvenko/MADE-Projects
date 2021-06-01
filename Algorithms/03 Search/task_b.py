"""Task B solution"""

import sys

def find_lower_bound(array, n, left=None, right=None):
    """FInds lower bound for n in sorted array"""
    if left and right:
        tmp_low = left
        tmp_up = right
    else:
        tmp_low = -1
        tmp_up = len(array)
    middle = tmp_up // 2
    
    while tmp_low < tmp_up - 1:
        if array[middle] >= n:
            tmp_up = middle
        else:
            tmp_low = middle
            
        middle = (tmp_up + tmp_low) // 2
        
    return tmp_up


def find_upper_bound(array, n, left=None, right=None):
    """Finds upper bound"""
    return find_lower_bound(array, n + 1, left, right)


def proceed_request(array, l_num, r_num):
    """Process request"""
    return find_upper_bound(array, r_num ) - find_lower_bound(array, l_num)


if __name__ == '__main__':
    _ = sys.stdin.readline() #no need for array length
    array = sys.stdin.readline().split()
    for i, cur in enumerate(array):
        array[i] = int(cur)
        
    array = sorted(array)
    
    n_requests = int(sys.stdin.readline())
    for _ in range(n_requests):
        left, right = map(int, sys.stdin.readline().split())
        sys.stdout.write(str(proceed_request(array, left, right)) + '\n')
