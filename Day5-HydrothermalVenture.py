# Given file of coordinate lines x1y1 -> x2y2
f = open("Day5-Input.txt")
lines = f.readlines()

# PART 1
# Determine the points where at least two lines overlap
# Consider only horizontal and vertical lines

# PART 2
# Consider diagonal lines as well

horiz = []
vert = []
diag = []
points = {}
overlap = 0

# Clean the input file
# Divide into horizontal, vertical, diagonal lines
for line in lines:
    delim1 = line.find(',')
    x1 = int(line[:delim1])
    delim2 = line.find('-')
    y1 = int(line[delim1 + 1:delim2])
    delim3 = line.find('>')
    delim4 = line.rfind(',')
    x2 = int(line[delim3 + 1:delim4])
    y2 = int(line[delim4 + 1:])
    if x1 == x2:
        horiz.append([x1, y1, x2, y2])
    if y1 == y2:
        vert.append([x1, y1, x2, y2])
    if abs(x1 - x2) == abs(y1 - y2):
        diag.append([x1, y1, x2, y2])

# Sample test provided
horiz_test = [[2, 2, 2, 1], [7, 0, 7, 4]]
vert_test = [[0, 9, 5, 9], [9, 4, 3, 4], [0, 9, 2, 9], [3, 4, 1, 4]]
diag_test = [[8, 0, 0, 8], [6, 4, 2, 0], [0, 0, 8, 8], [5, 5, 8, 2]]

# Add horizontal points and check overlap
for line in horiz:
    x, y1, y2 = line[0], line[1], line[3]
    for y in range(min(y1, y2), max(y1, y2) + 1):
        point = (x, y)
        if point in points:
            points[point] += 1
        else:
            points[point] = 1

# Add vertical points and check overlap
for line in vert:
    x1, y, x2 = line[0], line[1], line[2]
    for x in range(min(x1, x2), max(x1, x2) + 1):
        point = (x, y)
        if point in points:
            points[point] += 1
        else:
            points[point] = 1

# Add diagonal points and check overlap
for line in diag:
    x1, y1, x2, y2 = line[0], line[1], line[2], line[3]
    if x1 < x2 and y1 < y2:
        for i in range(x2 - x1 + 1):
            point = (x1 + i, y1 + i)
            if point in points:
                points[point] += 1
            else:
                points[point] = 1
    if x1 > x2 and y1 > y2:
        for i in range(x1 - x2 + 1):
            point = (x1 - i, y1 - i)
            if point in points:
                points[point] += 1
            else:
                points[point] = 1
    if x1 < x2 and y1 > y2:
        for i in range(x2 - x1 + 1):
            point = (x1 + i, y1 - i)
            if point in points:
                points[point] += 1
            else:
                points[point] = 1
    if x1 > x2 and y1 < y2:
        for i in range(x1 - x2 + 1):
            point = (x1 - i, y1 + i)
            if point in points:
                points[point] += 1
            else:
                points[point] = 1

# Count the number of overlaps
for point in points:
    if points[point] > 1:
        overlap += 1

print(overlap)