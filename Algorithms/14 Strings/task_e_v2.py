"""Task E solution"""

from collections import Counter
PRIME_P = 31
PRIME_M = 179424673

def cal_sub_hashes(string, n):
    """Calcs hashes for all substrings of length N"""
    p_n = 1
    hashes = [ord(string[0])]

    for idx in range(1, n):
        hashes.append((hashes[-1] * PRIME_P + ord(string[idx])) % PRIME_M)
        p_n = (p_n * PRIME_P) % PRIME_M

    for idx in range(n, len(string)):
        cur = (hashes[-1] - ord(string[idx - n]) * p_n) % PRIME_M
        cur = (cur * PRIME_P + ord(string[idx])) % PRIME_M
        hashes.append(cur)
    return hashes[n - 1:]

def check_for_sub_n(strings, n):
    """Checks, whether substring of length N is in all substrings"""
    all_hashes = Counter()
    for string in strings:
        all_hashes += Counter(set(cal_sub_hashes(string, n)))
    # all_hashes = sorted(all_hashes)
    # for idx in range(len(all_hashes) - len(strings) + 1):
    #     if all_hashes[idx] == all_hashes[idx + len(strings) - 1]:
    #         return all_hashes[idx]
    best = all_hashes.most_common(1)[0]
    if best[1] == len(strings):
        return best[0]
    return None

def bin_search(strings):
    left = 0
    right = 10 ** 10
    results = dict()
    for string in strings:
        right = min(right, len(string))
    right += 1

    while right - left > 1:
        mid = (right + left) // 2
        result = check_for_sub_n(strings, mid)
        # print(left, mid, right, result)
        results[mid] = result
        if result:
            left = mid
        else:
            right = mid
    return results[left], left

def solve(strings):
    h, left = bin_search(strings)
    hashes = cal_sub_hashes(strings[0], left)
    for i in range(len(hashes)):
        if hashes[i] == h:
            return strings[0][i:i + left]

if __name__ == '__main__':
    n = int(input())
    words = []
    for _ in range(n):
        words.append(input())
    print(solve(words))