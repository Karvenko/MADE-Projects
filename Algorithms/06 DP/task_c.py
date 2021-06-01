"""Task C solution"""

def nvp(array):
    dp = [1]
    seq = [[array[0]]]
    total_max = 1
    total_max_idx = 0
    for i, cur in enumerate(array):
        if i == 0:
            continue
        cur_len = 1
        cur_seq = [array[i]]
        for j in range(i - 1, -1, -1):
            if j < cur_len - 1: #early stoping
                break
            if cur > array[j]:
                if dp[j] >= cur_len:
                    cur_len = dp[j] + 1
                    tmp_arr = [x for x in seq[j]]
                    tmp_arr.append(cur)
                    cur_seq = tmp_arr
        dp.append(cur_len)
        seq.append(cur_seq)
        if cur_len > total_max:
            total_max = cur_len
            total_max_idx = i
    return total_max, seq[total_max_idx]

if __name__ == '__main__':
    _ = input()
    array = [int(x) for x in input().split()]
    n, res = nvp(array)
    res = map(str, res)
    print(n)
    print(' '.join(res))
    