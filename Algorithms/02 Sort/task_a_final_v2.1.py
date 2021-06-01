"""Task A solution"""
import sys


def q_split(a, start, end, piv):
    """Splitting array"""
    l = start
    r = end

    while l <= r:
        while a[l] < piv:
            l += 1

        while a[r] > piv:
            r -= 1

        if l <= r:
            a[l], a[r] = a[r], a[l]
            l += 1
            r -= 1

    return l, r


def k_find(a, start, end, k):
    """Finfing K stat"""
    if end - start == 0:
        return a[k]

    piv = a[start]
    left, right = q_split(a, start, end, piv)

    if left <= k and left < end:
        result = k_find(a, left, end, k)
    elif right >= k and right > start:
        result = k_find(a, start, right, k)
    else:
        result = a[k]

    return result


def copy_array(array, tmp_array, start, end):
    """copy data from original array to temp"""
    for i, cur in enumerate(array[start:end + 1]):
        tmp_array[i] = cur

    return


if __name__ == '__main__':

    _ = sys.stdin.readline()  # no need for str len
    arr = sys.stdin.readline().split()
    for i, cur in enumerate(arr):
        arr[i] = int(cur)
    tmp_arr = [0] * len(arr)

    n_req = int(sys.stdin.readline())

    for _ in range(n_req):
        start, end, k = map(int, sys.stdin.readline().split())
        start -= 1
        end -= 1
        k -= 1
        copy_array(arr, tmp_arr, start, end)
        sys.stdout.write(str(k_find(tmp_arr, 0, end - start, k)) + '\n')
