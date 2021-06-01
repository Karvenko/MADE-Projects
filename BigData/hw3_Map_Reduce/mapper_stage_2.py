#!/usr/bin/python3
import sys

#SELECT_YEARS = [2008, 2011]
#For prod
SELECT_YEARS = [2010, 2016]

for line in sys.stdin:
    year, count, tag = line.split()
    if int(year) in SELECT_YEARS:
        sys.stdout.write(f'{year}\t{count}\t{tag}\n')
