"""Task C solution"""

import sys

SEPARATOR = "\n"
UNICODE = "utf-8"

class FenvicTree():
    def __init__(self, a):
        self.a = a
        self.t = self.gen_f_sums()
        
    def fen(self, i):
        return i & (i + 1)
    
    def gen_f_sums(self):
        t = []
        for i in range(len(self.a)):
            tmp = 0
            j = self.fen(i)
            for k in range(j, i + 1):
                tmp += self.a[k]
            t.append(tmp)
        return t
    
    def get(self, i):
        res  = 0
        j = i
        while j >= 0:
            res += self.t[j]
            j = self.fen(j) - 1
        return res
    
    def rsq(self, left, right):
        if left == 0:
            return self.get(right)
        else:
            return self.get(right) - self.get(left - 1)
        
    def add(self, i, x):
        j = i
        while j < len(self.t):
            self.t[j] += x
            j = j | (j + 1)
        self.a[i] += x
        
    def set_val(self, i, x):
        d = x - self.a[i]
        self.add(i, d)
        
if __name__ == '__main__':
    result = []
    data = sys.stdin.buffer.read().splitlines()
    a = [int(x) for x in data[1].decode(UNICODE).split()]
    
    ft = FenvicTree(a)
    
    for line in data[2:]:
        command, idx, val = line.decode(UNICODE).split()
        if command == 'sum':
            result.append(str(ft.rsq(int(idx) - 1, int(val) - 1)))
        else:
            ft.set_val(int(idx) - 1, int(val))
            
    sys.stdout.buffer.write((SEPARATOR.join(result)).encode(UNICODE))