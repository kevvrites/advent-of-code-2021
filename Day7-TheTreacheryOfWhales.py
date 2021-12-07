import math

# Given a list of horizontal positions
f = open("Day7-Input.txt")
horiz = [int(num) for num in f.readlines()[0].split(',')]
horiz.sort()

# PART 1
# Find the least distance along all numbers to a common number
# Median is the optimal number
# Return fuel (fuel = distance)

# PART 2
# Fuel is now growing over time (e.g. 1+2+3+4)
# Mean is the optimal number
# Return fuel

average_low = math.floor(sum(horiz) / len(horiz))
average_high = math.ceil(sum(horiz) / len(horiz))
median = horiz[len(horiz) // 2]

fuel = 0
for pos in horiz:
    fuel += abs(pos - median)
print(fuel)

fuel_low = 0
fuel_high = 0
for pos in horiz:
    distance_low = abs(pos - average_low)
    distance_high = abs(pos - average_high)
    fuel_low += distance_low * (distance_low + 1) // 2
    fuel_high += distance_high * (distance_high + 1) // 2
print(fuel_low, fuel_high)