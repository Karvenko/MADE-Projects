"""Task C solution"""
SEP = '#'

def p_function(s):
    p = [0] * len(s)
    for i in range(1, len(s)):
        k = p[i - 1]
        while k > 0 and s[i] != s[k]:
            k = p[k - 1]
        if s[i] == s[k]:
            k += 1
        p[i] = k
    return p

def kmp(p, t):
    pref = p_function(p + SEP + t)[-len(t):]
    result = []
    for idx in range(len(t)):
        if pref[idx] == len(p):
            result.append(idx - len(p) + 2) # adding 2 to get answers starting from 1
    return result

if __name__ == '__main__':
    p = input()
    t = input()
    res = kmp(p, t)
    print(len(res))
    print(*res)