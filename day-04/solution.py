#!/usr/bin/env python
import sys
import re

def get_guard_id(line):
    m = re.search('#([\d]+)', line)
    return int(m.group(1))

def get_date_time(line):
    m = re.search('-(\d{2}\-\d{2}) \d{2}:(\d{2})', line)
    return (m.group(1), int(m.group(2)))

def get_last_asleep(watch, time):
    for i in range(time, 0, -1):
        if watch[i] == True:
            return i
    return 0

def record_event(line, current_guard, watches):
    date, time = get_date_time(line)
    print(f'{date} {time}')
    if date not in watches[current_guard].keys():
        watch = [False] * 60
        watches[current_guard][date] = watch

    watch = watches[current_guard][date]

    if "asleep" in line:
        watch[time] = True
    else:
        last_asleep = get_last_asleep(watch, time)
        for i in range(last_asleep, time):
            watch[i] = True
        watch[time] = False

input = sys.stdin.readlines()
input.sort()
watches = dict()
current_guard = 0
watches[current_guard] = dict()

for line in input:
    if "Guard" in line:
        current_guard = get_guard_id(line)
        if current_guard not in watches:
            watches[current_guard] = dict()
    else:
        record_event(line, current_guard, watches)


sleepiest = 0
sleepiest_minute = 0
sleepiest_minute_count = 0
sleepiest_guard = 0

for guard in watches.keys():
    sleep_log = [0] * 60
    for date in watches[guard].keys():
        watch = watches[guard][date]
        for i in range(0, 59):
            if watch[i] == True:
                sleep_log[i] += 1
    total_sleep = sum(sleep_log)
    if total_sleep > sleepiest:
        sleepiest = total_sleep
        sleepiest_guard = guard
        sleepiest_minute_count = max(sleep_log)
        sleepiest_minute = sleep_log.index(sleepiest_minute_count)
print(f'Guard {sleepiest_guard} slept for {sleepiest}, {sleepiest_minute} ({sleepiest_minute_count})')
print(f'Solution: {sleepiest_guard * sleepiest_minute}')