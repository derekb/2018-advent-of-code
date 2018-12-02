
#!/usr/bin/env python
import sys

input = [line.strip() for line in sys.stdin.readlines()]

twos = 0
threes = 0

for id in input:
    for other_id in input:
        diff = 0
        for pos, char in enumerate(id):
            if other_id[pos] != char:
                diff += 1
        if diff == 1:
            for pos, char in enumerate(id):
                if other_id[pos] == char:
                    print(char, end="")
            exit()
raise Exception