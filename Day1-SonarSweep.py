# Given text file with 1 number on each line
# First line does not count as increment.

f = open("Day1-Input.txt")
lines = f.readlines()

# PART 1
# Return the number of times the number increases from prior lines.

firstLine = int(lines[0])
prevLine = firstLine
count1 = 0

for line in lines:
    if int(line) > int(prevLine):
        count1 += 1
    prevLine = line
print(count1)

# PART 2
# Implement a sliding window of size 3
# Determine if the sum of the sliding window increases from the previous.

winStart = 0
prevSum = int(lines[0]) + int(lines[1]) + int(lines[2])
currSum = 0
count2 = 0

for winEnd, value in enumerate(lines):
    currSum += int(value)
    if winEnd - winStart + 1 == 3:
        if currSum > prevSum:
            count2 += 1
        prevSum = currSum
        currSum -= int(lines[winStart])
        winStart += 1
print(count2)