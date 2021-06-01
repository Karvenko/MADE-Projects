def my_sum(a, b):
    return a + b

if __name__ == '__main__':
    t = int(input())
    
    for i in range(t):
        a, b = input().split()
        print(my_sum(int(a), int(b)))