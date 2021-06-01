#!/usr/bin/python3
import sys
import random

SHUFFLE_CONSTANT = 42424242

for line in sys.stdin:
    sys.stdout.write(f'{random.randint(0, SHUFFLE_CONSTANT)} {line}')
