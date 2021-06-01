"""Task A solution"""
VERY_SMALL_NUMBER = -(10 ** 12)

def find_way(rewards, k):
    n = len(rewards)
    prevs = [0] * n
    collected = [0] * n
    prevs[0] = -1
    collected[0] = 0
    
    for i in range(1, n):
        best_move = -1 
        best_result = VERY_SMALL_NUMBER
        for j in range(1, min(i, k) + 1):
            if collected[i - j] > best_result: #checking for best previous step
                best_move = i - j
                best_result = collected[i - j]
        collected[i] = best_result + rewards[i]
        prevs[i] = best_move
        
    result = [n - 1]
    i = n - 1
    while i > 0:
        result.append(prevs[i])
        i = prevs[i]
    return collected[-1], [x + 1 for x in result[::-1]]

if __name__ == '__main__':
    n, k = map(int, input().split())
    rewards = [0] * n
    tmp_r = map(int, input().split())
    for i, cur in enumerate(tmp_r):
        rewards[i + 1] = cur
        
    collected, steps = find_way(rewards, k)
    print(collected)
    print(len(steps) - 1)
    steps = map(str, steps)
    print(' '.join(steps))
