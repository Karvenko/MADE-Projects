"""Task D solution"""

def levenstein(a, b):
    if len(a) == 0:
        return len(b)
    if len(b) == 0:
        return len(a)
    dp = [[0 for j in range(len(b) + 1)] for i in range(len(a) + 1)]
    for i in range(len(a) + 1):
        dp[i][0] = i
    for j in range(len(b) + 1):
        dp[0][j] = j
        
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
    return dp[i][j]

if __name__ == '__main__':
    str1 = input()
    str2 = input()
    print(levenstein(str1, str2))
