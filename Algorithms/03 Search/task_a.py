"""Task a solution"""

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


def proceed_request(array, n):
    result = 0
    
    if array[0] >= n:
        return array[0]
    if array[-1] <= n:
        return array[-1]
    
    idx = find_lower_bound(array, n)
    if array[idx] == n:
        result = array[idx]
    else:
        diff_low = n - array[idx - 1]
        diff_high = array[idx] - n
        if diff_low <= diff_high:
            result = array[idx - 1]
        else:
            result = array[idx]
            
    return result


if __name__ == '__main__':
    _ = sys.stdin.readline() #no need for array length
    array = sys.stdin.readline().split()
    for i, cur in enumerate(array):
        array[i] = int(cur)
        
    requests = sys.stdin.readline().split()
    for cur in requests:
        sys.stdout.write(str(proceed_request(array, int(cur))) + '\n')
        
        