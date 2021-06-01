import sys

SEPARATOR = "\n"
UNICODE = "utf-8"
INF = 10 ** 10

def int_log(n):
    if n == 1 or n == 0:
        return 0
    
    min_pow = 2
    k = 1
    while min_pow < n:
        min_pow *= 2
        k += 1
        
    return k


def fill_min_table(n, a0):
    log_n = int_log(n)
    min_table = [[0 for i in range(2 * log_n + 1)] for j in range(2 * n)]
    
    pow_array = [1]
    for i in range(1, 25):
        pow_array.append(pow_array[-1] * 2)
    
    min_table[0][0] = a0
    for i in range(1, n):
        min_table[i][0] = (23 * min_table[i - 1][0] + 21563) % 16714589
    for j in range(1, log_n):
        for i in range(n):
            min_table[i][j] = min(min_table[i][j - 1], min_table[i + pow_array[j - 1]][j - 1])
    return min_table


def process_req(n, m, a0, u0, v0):
    log_array = [0, 0]
    max_pow = 2
    k = 1
    for i in range(2, n + 2):
        if i > max_pow:
            max_pow *= 2
            k += 1
        log_array.append(k - 1)
        
    pow_array = [1]
    for i in range(1, log_array[-1] + 1):
        pow_array.append(pow_array[-1] * 2)
        
    min_table = fill_min_table(n, a0)
    
    u = u0
    v = v0
    left = min(u, v) - 1
    right = max(u, v)
    k = log_array[right - left + 1]
    r = min(min_table[left][k], min_table[right - pow_array[k]][k])
    
    for i in range(1, m):
        u = (17 * u + 751 + r + 2 * i) % n + 1
        v = (13 * v + 593 + r + 5 * i) % n + 1
        if u < v:
            left = u - 1
            right = v
        else:
            left = v - 1
            right = u
        k = log_array[right - left + 1]
        r = min(min_table[left][k], min_table[right - pow_array[k]][k])
        
    return u, v, r

if __name__ == '__main__':
    result = [0, 0, 0]
    data = sys.stdin.buffer.read().splitlines()
    n, m, a1 = map(int, data[0].decode(UNICODE).split())
    u1, v1 = map(int, data[1].decode(UNICODE).split())
    
    result[0], result[1], result[2] = map(str, process_req(n, m, a1, u1, v1))
    sys.stdout.buffer.write((SEPARATOR.join(result)).encode(UNICODE))
    
