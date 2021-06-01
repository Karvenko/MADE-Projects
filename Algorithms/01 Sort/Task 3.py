def merge(a, b):
    len_a = len(a)
    len_b = len(b)
    c = [0] * (len_a + len_b) #final array
    
    i = 0
    j = 0
    while i + j < len_a + len_b:
        if j == len_b or (i < len_a and a[i] < b[j]):
            c[i+j] = a[i]
            i += 1
        else:
            c[i+j] = b[j]
            j += 1
            
    return c

def merge_sort(a):
    len_a = len(a)
    if len_a == 1:
        return a
    
    left = merge_sort(a[:int(len_a/2)])
    right = merge_sort(a[int(len_a/2):])
    
    return merge(left, right)

if __name__ == '__main__':
    t = input() #no need for length in Python
    
    a = input().split()
    for i in range(len(a)): #convert to int inplace
        a[i] = int(a[i])
        
    a = merge_sort(a)
    
    #Make output string
    out_str = str()
    for cur in a:
        out_str += str(cur)
        out_str += ' '
        
    print(out_str[:-1])