#!/usr/bin/env python
import sys
import re

class Claim:
    def __init__(self, id, x, y, x_len, y_len):
        self.id = id
        self.x = int(x)
        self.y = int(y)
        self.x_len = int(x_len)
        self.y_len = int(y_len)

def get_claim(line):
    m = re.search('#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)', line)
    return Claim(m.group(1), m.group(2), m.group(3), m.group(4), m.group(5))

def stake_claim(claim, matrix):
    return 0

input = sys.stdin.readlines()
claims = [get_claim(line.strip()) for line in input]

marks = dict()

for claim in claims:
    for i in range(claim.x, claim.x+claim.x_len):
        if i not in marks.keys():
            marks[i] = dict()
        for j in range(claim.y, claim.y+claim.y_len):
            if j not in marks[i].keys():
                marks[i][j] = 0
            marks[i][j] += 1

overlap_inches = 0

for key in marks.keys():
    overlap_inches += len([val for val in marks[key].values() if val > 1])

print(overlap_inches)