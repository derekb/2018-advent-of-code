#!/usr/bin/env python
import sys

def get_letter_counts(id):
    counts = dict()
    for c in id:
        if c in counts.keys():
            counts[c] += 1
        else:
            counts[c] = 1
    return counts

input = sys.stdin.readlines()

twos = 0
threes = 0

for id in input:
    counts = get_letter_counts(id)
    values = counts.values()
    if any(x == 2 for x in values):
        twos += 1
    if any(x == 3 for x in values):
        threes += 1

print(twos)
print(threes)
print (twos * threes)