# Given input with smoke point locations
f = open("Day9-Input.txt")
locations = f.readlines()

blank = ''
for i in range(103):
    blank += '9'

def convert(string):
    list1 = []
    list1[:0] = string
    return list1

locations.insert(0, blank)
locations.insert(len(locations), blank)

for idx, line in enumerate(locations):
    line = '9{}9'.format(line.strip())
    locations[idx] = convert(line)

# PART 1
# Find all the low points in the map
# Return their risk sum (risk = height + 1)
lowpoints = []
lowcoor = [] 
for y in range(1, len(locations) - 1):
    for x in range(1, len(locations[y]) - 1):
        center = locations[y][x]
        up = locations[y-1][x]
        left = locations[y][x-1]
        right = locations[y][x+1]
        down = locations[y+1][x]
        if center < up and center < left and center < right and center < down:
            lowpoints.append(center)
            lowcoor.append((y, x))

ans = 0
for point in lowpoints:
    ans += int(point) + 1
print(ans)

# PART 2
# Find the 3 largest basin sizes and return their product
marked = []
def basinSize(y, x):
    size = 0
    center = int(locations[y][x])
    up = int(locations[y-1][x])
    left = int(locations[y][x-1])
    right = int(locations[y][x+1])
    down = int(locations[y+1][x])
    if up != 9 and up > center:
        if (y-1, x) not in marked:
            size += int(basinSize(y-1, x))
            marked.append((y-1, x))
    if left != 9 and left > center:
        if (y, x-1) not in marked:
            size += int(basinSize(y, x-1))
            marked.append((y, x-1))  
    if right != 9 and right > center:
        if (y, x+1) not in marked:
            size += int(basinSize(y, x+1))
            marked.append((y, x+1))
    if down != 9 and down > center:
        if (y+1, x) not in marked:
            size += int(basinSize(y+1, x))
            marked.append((y+1, x))
    size += 1
    return int(size)

basins = []
for i in range(len(lowcoor)):
    y, x = lowcoor[i][0], lowcoor[i][1]
    basin_size = basinSize(y, x)
    basins.append(basin_size)

basins.sort(reverse = True)
print(basins[0] * basins[1] * basins[2])