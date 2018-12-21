#!/bin/python3
# Data format: [yyyy-mm-dd hh:mm] Message
# Message:  Gaurd #\d
#           fall
#           wake

## Part 1 ##
# Find the gaurd who is awake for the same minute the most. Return the gaurd's number times the minute

# Parse the time, sort by that.
# Then find gaurds and start compiling times they are awake or asleep.
# Then sum the overlap.

def date_parse(date, time):
    month = int(date[:2])
    day = int(date[3:])

    if int(time) != 0:
        if (day < 31 and month in [1,3,5,7,8,10,12]) or (day < 30 and month not in [1,3,5,7,8,10,12]):
            day += 1
        else:
            month += 1
            day = 1

    return str(month) + '-' + str(day)
    

import sys

lines = list(map(lambda s : s.strip(), open(sys.argv[1], 'r')))
parsed = [
        (date_parse(line[6:11], line[12:14]),
        int(line[15:17]) if int(line[12:14]) == 0 else int(line[15:17]) - 60,
        line[19:])
    for line in lines ]
dates = { date[0] : {} for date in parsed }
gaurd_nums = set()
for message in parsed:
    info = message[2]
    if 'fall' in info:
        info = 'f'
    elif 'wake' in info:
        info = 'w'
    else:
        info = int(info[info.find('#') + 1 : info.find(' ', info.find('#'))])
        gaurd_nums.add(info)
    dates[message[0]][message[1]] = info

gaurds = { num : [] for num in gaurd_nums}
for date, night in dates.items():
    sort = sorted(night)
    gaurd = night[sort[0]]
    times = [1]*60
    write = 0
    for i in range(0,60):
        if i in sort[1:]:
            if night[i] == 'f':
                write = 1
            else:
                write = 0
        times[i] = write
    gaurds[gaurd].append(times)

maxes = dict()
for gaurd in gaurds:
    minutes = [0]*60
    for day in gaurds[gaurd]:
        for i in range(0, len(minutes)):
            minutes[i] += day[i]
    gaurds[gaurd] = minutes
    maxes[gaurd] = max(minutes)

max_num = 0
max_sum = 0
max_gaurd = 0
part_2_max_gaurd = list(gaurds.keys())[0]
for gaurd in maxes:
    if sum(gaurds[gaurd]) > max_sum:
        max_gaurd = gaurd
        max_sum = sum(gaurds[gaurd])
    if maxes[gaurd] > maxes[part_2_max_gaurd]:
        part_2_max_gaurd = gaurd

## Part 1 ##
for minute in range(len(gaurds[max_gaurd])):
    if gaurds[max_gaurd][minute] == maxes[max_gaurd]:
        print(max_gaurd*minute)

## Part 2 ##
for minute in range(len(gaurds[part_2_max_gaurd])):
    if gaurds[part_2_max_gaurd][minute] == maxes[part_2_max_gaurd]:
        print(part_2_max_gaurd*minute)
