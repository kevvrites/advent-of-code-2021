# Given an list of countdown timers
from typing import Counter


f = open("Day6-Input.txt")
lines = f.readlines()[0]

timers = [int(i) for i in lines.split(',')]

# PART 1
# Find a way to calculate growth rate
# Return the 80 day population count

# This also modifies the input list directly
def calcGrowth(timers, time):
    for day in range(time):
        for timer in range(len(timers)):
            if timers[timer] == 0:
                timers[timer] = 6
                timers.append(8)
            else:
                timers[timer] -= 1
    return(len(timers))

# PART 2
# Return the 256 day population count
# Requires a more time-efficient solution

def calcGrowth2(timers, time):
    fish_count = [0 for i in range(9)]
    for timer in timers:
        fish_count[timer] += 1
    for day in range(time):
        new_fish = [0 for i in range(9)]
        for timer, count in enumerate(fish_count):
            if timer == 0:
                new_fish[6] += count
                new_fish[8] += count
            else:
                new_fish[timer-1] += count
        fish_count = new_fish
    return(sum(fish_count))

#print(calcGrowth(timers,80))
print(calcGrowth2(timers, 256))