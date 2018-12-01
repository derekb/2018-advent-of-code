#!/usr/bin/env python

import sys

input = [int(line) for line in sys.stdin.readlines()]
seen = set()
frequency = 0
seen.add(frequency)

while len(input) != 0:
    next = input.pop(0)
    input.append(next)
    frequency = frequency + next

    if frequency not in seen:
        seen.add(frequency)
    else:
        print(frequency)
        exit()