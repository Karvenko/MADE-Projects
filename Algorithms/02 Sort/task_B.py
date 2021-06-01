"""Task B solution"""
MAX_NUM = 101 #It should be max N + 1 to correct handle zero

def count_sort(a):
    """Count sort for array a"""
    cnt = [0] * MAX_NUM

    for cur in a:
        cnt[cur] += 1

    i = 0
    for j in range(MAX_NUM):
        while cnt[j] > 0:
            a[i] = j
            cnt[j] -= 1
            i += 1

    return a

if __name__ == '__main__':

    array = input().split()
    for i, cur in enumerate(array): #convert to int inplace
        array[i] = int(cur)

    array = count_sort(array)

    #Make output string
    out_str = str()
    for cur in array:
        out_str += str(cur)
        out_str += ' '

    print(out_str[:-1])
