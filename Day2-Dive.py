# Given text file with each line containing a direction and a value
f = open("Day2-Input.txt")
directions = f.readlines()

# PART 1
# Calculate the total in two directions
# Return their product
horiz = 0
vert = 0

for each in directions:
    dir, val = each.split(" ")
    if dir == "forward":
        horiz += int(val)
    if dir == "down":
        vert += int(val)
    if dir == "up":
        vert -= int(val)
print(horiz * vert)

# PART 2
# Up and down change a new variable called aim
# Aim affects the vertical position when forward is called
# Return their product

horiz2 = 0
vert2 = 0
aim = 0

for each in directions:
    dir, val = each.split(" ")
    if dir == "forward":
        horiz2 += int(val)
        vert2 += (aim * int(val))
    if dir == "down":
        aim += int(val)
    if dir == "up":
        aim -= int(val)
print(horiz2 * vert2)