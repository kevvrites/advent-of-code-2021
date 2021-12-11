# Given input is lines with just symbols
f = open("Day10-Input.txt")
lines = f.readlines()

# PART 1
# Find the first error in each line and return the score
symbols = {')':'(', ']':'[', '}':'{', '>':'<'}

ans = []
corrupted = []
for line in range(len(lines)):
    stack = []
    for char in lines[line]:
        if char in symbols:
            if stack and stack[-1] == symbols[char]:
                stack.pop()
            else:
                ans.append(char)
                corrupted.append(line)
                break
        else:
            stack.append(char)
        
score = 0
for char in ans:
    if char == ')':
        score += 3
    if char == ']':
        score += 57
    if char == '}':
        score += 1197
    if char == '>':
        score += 25137
print(score)

# PART 2
# Complete the incomplete lines and return their score

# Remove the corrupted lines
corrupted.sort(reverse=True)
for num in corrupted:
    lines.pop(num)

symbols2 = {'(':')', '[':']', '{':'}', '<':'>'}

scores2 = []
for line in lines:
    stack = []
    complete = []
    score2 = 0
    for char in line.strip():
        if char in symbols:
            if stack and stack[-1] == symbols[char]:
                stack.pop()
        else:
            stack.append(char)
    for char in stack:
        complete.append(symbols2[char])
    for char in complete[::-1]:
        score2 *= 5
        if char == ')':
            score2 += 1
        if char == ']':
            score2 += 2
        if char == '}':
            score2 += 3
        if char == '>':
            score2 += 4
    scores2.append(score2)

scores2.sort()
print(scores2[(len(scores2) // 2)])