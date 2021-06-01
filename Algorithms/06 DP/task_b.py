"""Task A solution"""
VERY_SMALL_NUMBER = -(10 ** 12)

def find_way(rewards, n, m):
    prevs = [[-1 for i in range(m)] for j in range(n)]
    collected = [[VERY_SMALL_NUMBER for i in range(m + 1)] for j in range(n + 1)]
    
    collected[1][1] = rewards[1][1]
    
    #First line
    i = 1
    for j in range(2, m + 1):
        collected[i][j] = collected[i][j - 1] + rewards[i][j]
        prevs[i - 1][j - 1] = 'R'
        
    for i in range(2, n + 1):
        for j in range(1, m + 1):
            if collected[i - 1][j] >= collected[i][j - 1]:
                prevs[i - 1][j - 1] = 'D'
                collected[i][j] = collected[i - 1][j] + rewards[i][j]
            else:
                prevs[i - 1][j - 1] = 'R'
                collected[i][j] = collected[i][j - 1] + rewards[i][j]
                
    result = []
    i = n - 1
    j = m - 1
    while i > 0 or j > 0:
        result.append(prevs[i][j])
        if prevs[i][j] == 'D':
            i -= 1
        else:
            j -= 1
                
    return collected[n][m], result[::-1]

if __name__ == '__main__':
    n, m = map(int, input().split())
    rewards = [[VERY_SMALL_NUMBER for i in range(m + 1)] for j in range(n + 1)]
    for row in range(1, n + 1):
        tmp_r = map(int, input().split())
        for i, cur in enumerate(tmp_r):
            rewards[row][i + 1] = cur
        
    collected, steps = find_way(rewards, n, m)
    print(collected)
#     print(len(steps) - 1)
    steps = map(str, steps)
    print(''.join(steps))
