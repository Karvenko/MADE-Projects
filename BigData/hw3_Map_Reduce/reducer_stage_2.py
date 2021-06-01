#!/usr/bin/python3

import sys

MAX_STRINGS = 10

cur_year = -1
str_count = 0

for line in sys.stdin:
    year, count, tag = line.split()
    if int(year) != cur_year:
        cur_year = int(year)
        sys.stdout.write(f'{year}\t{tag}\t{count}\n')
        str_count = 1
    elif str_count < MAX_STRINGS:
        sys.stdout.write(f'{year}\t{tag}\t{count}\n')
        str_count += 1
    else:
        continue
