#!/usr/bin/python3
import sys
import random

MAX_LEN = 5

cur_seq = []
cur_seq_len = random.randint(1, 5)
count = 0
for line in sys.stdin:
    _, key = line.split()
    cur_seq.append(key)
    count += 1
    if count == cur_seq_len:
        sys.stdout.write(','.join(cur_seq))
        sys.stdout.write('\n')
        cur_seq = []
        count = 0
        cur_seq_len = random.randint(1, 5)

if count >= 0:
    sys.stdout.write(','.join(cur_seq))
    sys.stdout.write('\n')
