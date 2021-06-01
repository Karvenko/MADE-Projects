import sys

PRIME_P = 31
PRIME_M = 179424673
def get_p_pows(n, p=PRIME_P):
    """Returns array of powers of p from 0 to n-1"""
    result = [1]
    for _ in range(1, n):
        result.append(result[-1] * p % PRIME_M)
    return result

class StringChecker:
    def __init__(self, string):
        self.string = string
        self.hashes = self.get_hashes()
        self.ps = get_p_pows(n=len(string))

    def get_hashes(self):
        result = [ord(self.string[0])]
        for c in self.string[1:]:
            result.append((result[-1] * PRIME_P + ord(c)) % PRIME_M)
        return result

    def get_substring_hash(self, l, r):
        if l == 0:
            return self.hashes[r]

        return (self.hashes[r] - self.hashes[l - 1] * self.ps[r - l + 1]) % PRIME_M

    def query(self, a, b, c, d):
        if b - a != d - c:
            return False
        return self.get_substring_hash(a, b) == self.get_substring_hash(c, d)

if __name__ == '__main__':
    data = sys.stdin.readlines()
    sc = StringChecker(data[0])
    result = []
    for query in data[2:]:
        a, b, c, d = map(int, query.split())
        result.append('Yes' if sc.query(a - 1, b - 1, c - 1, d - 1)
                      else 'No')
    sys.stdout.write('\n'.join(result))

