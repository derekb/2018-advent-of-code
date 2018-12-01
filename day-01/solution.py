#!/usr/bin/env python

import sys

input = []

for line in sys.stdin:
    input.append(int(line))

print (sum(input))