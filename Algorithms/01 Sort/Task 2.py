def bubble_sort(a):
    len_a = len(a) - 1
    
    changes = 1 #swap counter
    while changes > 0:
        changes = 0
        for idx in range(len_a):
            if a[idx] > a[idx+1]:
                a[idx], a[idx+1] = a[idx+1], a[idx]
                changes += 1
                
    return a

if __name__ == '__main__':
    t = input() #no need for length in Python
    
    a = input().split()
    for i in range(len(a)): #convert to int inplace
        a[i] = int(a[i])
        
    a = bubble_sort(a)
    
    #Make output string
    out_str = str()
    for cur in a:
        out_str += str(cur)
        out_str += ' '
        
    print(out_str[:-1])