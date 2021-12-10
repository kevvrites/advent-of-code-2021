# Given a list of signals corresponding to seven digits
# abcdefg are segments of the seven digit display
# Each line has 10 signals, then | delimiter, then four output numbers
f = open("Day8-Input.txt")
lines = f.readlines()

# 0 = abcefg, len = 6
# 1 = cf, len = 2
# 2 = acdeg, len = 5
# 3 = acdfg, len = 5
# 4 = bcdf, len = 4
# 5 = abdfg, len = 5
# 6 = abdefg, len = 6
# 7 = acf, len = 3
# 8 = abcdefg, len = 7
# 9 = abcdfg, len = 6

# Unique numbers: 1 (2), 4 (4), 7 (3), 8 (7)
# Non-unique numbers: 2, 3, 5 (5); 0, 6, 9 (6)

# PART 1
# Find how many times the digits 1, 4, 7, and 8 appear in output

counter = [0 for i in range(10)]
outputs = []
# for line in lines:
#     divide = line.find('|')
#     ten_digits = line[:divide].split(' ')
#     output = line[divide + 2:].strip().split(' ')
#     words = line.split(' ')
#     for digit in output:
#         if len(digit) == 2:
#             counter[1] += 1
#         if len(digit) == 4:
#             counter[4] += 1
#         if len(digit) == 3:
#             counter[7] += 1
#         if len(digit) == 7:
#             counter[8] += 1
#     for digit in ten_digits:
#         if len(digit) == 2:
#             seg25 = digit
#         if len(digit) == 4:
#             seg1235 = digit
#         if len(digit) == 3:
#             seg025 = digit
#         if len(digit) == 7:
#             pass
# print(counter[1] + counter[4] + counter[7] + counter[8])


# PART 2
# Decode the signals and sum the outputs
for line in lines:
    divide = line.find('|')
    ten_digits = line[:divide].split(' ')
    output = line[divide + 2:].strip().split(' ')
    find_digit = []
    code = ""
    for digit in ten_digits:
        if len(digit) == 2:
            seg1 = set([digit[i] for i in range(2)])
        if len(digit) == 4:
            seg4 = set([digit[i] for i in range(4)])
        if len(digit) == 3:
            seg7 = set([digit[i] for i in range(3)])
        if len(digit) == 7:
            seg8 = set([digit[i] for i in range(7)])
        else:
            find_digit.append(digit)
    for digit in find_digit:
        temp_set = set([digit[i] for i in range(len(digit))])
        if len(digit) == 5:
            if temp_set.issuperset(seg1):
                seg3 = temp_set
            elif len(temp_set.difference(seg4)) == 3:
                seg2 = temp_set
            else:
                seg5 = temp_set
        elif len(digit) == 6:
            if temp_set.issuperset(seg4):
                seg9 = temp_set
            elif temp_set.issuperset(seg7):
                seg0 = temp_set
            else:
                seg6 = temp_set
    for output in output:
        if len(output) == 2:
            decode = 1
        elif len(output) == 4:
            decode = 4
        elif len(output) == 3:
            decode = 7
        elif len(output) == 7:
            decode = 8
        else:
            output_set = set(output[i] for i in range(len(output)))
            if output_set == seg0:
                decode = 0
            if output_set == seg2:
                decode = 2
            if output_set == seg3:
                decode = 3
            if output_set == seg5:
                decode = 5
            if output_set == seg6:
                decode = 6
            if output_set == seg9:
                decode = 9
        code += str(decode)
    outputs.append(code)

total = 0
for num in range(len(outputs)):
    total += int(outputs[num])

print(total)