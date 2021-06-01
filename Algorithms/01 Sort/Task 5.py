import random
def q_sort(a, start, end):
    
    if end - start < 1:
        return
    
    l = start
    r = end
    
    piv = random.choice(a[start:end+1])
    
    while l <= r:
        while a[l] < piv:
            l += 1
            
        while a[r] > piv:
            r -= 1
            
        if l <= r:
            a[l], a[r] = a[r], a[l]
            l += 1
            r -= 1
            
    if start < r:
        q_sort(a, start, r)
        
    if end > l:
        q_sort(a, l, end)

if __name__ == '__main__':
    t = input() #no need for length in Python
    
    a = input().split()
    for i in range(len(a)): #convert to int inplace
        a[i] = int(a[i])
        
    q_sort(a, 0, len(a)-1)
    
    #Make output string
    out_str = str()
    for cur in a:
        out_str += str(cur)
        out_str += ' '
        
    print(out_str[:-1])