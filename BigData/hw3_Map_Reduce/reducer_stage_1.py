#!/usr/bin/python3

import sys
from collections import Counter

tag_counter = Counter()
for line in sys.stdin:
    year, count, tag = line.split()
    tag_counter[(year, tag)] += int(count)
    
for key, value in tag_counter.items():
    sys.stdout.write(f'{key[0]}\t{value}\t{key[1]}\n')
