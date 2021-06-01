def merge(a, b):
    len_a = len(a)
    len_b = len(b)
    c = [0] * (len_a + len_b) #final array
    
    inverse_count = 0
    
    i = 0
    j = 0
    while i + j < len_a + len_b:
        if j == len_b or (i < len_a and a[i] < b[j]):
            c[i+j] = a[i]
            i += 1
        else:
            c[i+j] = b[j]
            inverse_count += len_a - i
            j += 1
            
    return c, inverse_count

def merge_sort(a):
    len_a = len(a)
    if len_a == 1:
        return a, 0
    
    left, l_i = merge_sort(a[:int(len_a/2)])
    right, r_i = merge_sort(a[int(len_a/2):])
    
    arr, inverse_count = merge(left, right)
    
    return arr, inverse_count + l_i + r_i

if __name__ == '__main__':
    t = input() #no need for length in Python
    
    a = input().split()
    for i in range(len(a)): #convert to int inplace
        a[i] = int(a[i])
        
    a, inverse_count = merge_sort(a)
    
    print(inverse_count)