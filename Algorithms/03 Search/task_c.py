"""Task C solution"""
import math

EPS = 1e-15


def find_root(func, low, high):
    n_iter = math.ceil(math.log2((high - low) / EPS))
    
    tmp_low = low
    tmp_high = high
    middle = (tmp_high - tmp_low) / 2 + tmp_low
    
    for _ in range(n_iter):
        if func(middle) > 0:
            tmp_high = middle
        else:
            tmp_low = middle
        middle = (tmp_high - tmp_low) / 2 + tmp_low
        
    return middle


if __name__ == '__main__':
    c_param = float(input())
    
    print(find_root(lambda x: x ** 2 + math.sqrt(x) - c_param, 
                    0, math.sqrt(c_param))) #root must be in [0, sqrt(C)]
