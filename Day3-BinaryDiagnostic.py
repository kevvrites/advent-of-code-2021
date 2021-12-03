f = open("Day3-Input.txt")
lines = f.readlines()

# PART 1
# Find the most common bit in each position
# Find the least common bit in each position
# Return their decimal product
hashmap = {}
gamma = ""
epsilon = ""

for i in range(0, 12):
    hashmap[i] = 0

for line in lines:
    line = line.strip()
    for num in range(len(line)):
        if line[num] == "1":
            hashmap[num] += 1
        else:
            hashmap[num] -= 1

for key, val in hashmap.items():
    if val < 0:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"

gamma_decimal = int(gamma, 2)
epsilon_decimal = int(epsilon, 2)
print(gamma_decimal * epsilon_decimal)

print(gamma, epsilon)

# PART 2
# Oxygen = common, CO2 = uncommon
# Find the most un/common bit in the first position
# Then remove all non-matching entries
# Then find the most common bit among remaining
# Repeat until only 1 entry left
# Return oxygen * co2 decimal product
def oxygenGeneratorRating(nums):
    digit = 0
    common = 0

    for i in range(12):
        hashmap[i] = 0
    while len(nums) > 1:
        for row in range(len(nums)):
            nums[row] = nums[row].strip()
            if nums[row][digit] == "1":
                hashmap[digit] += 1
            else:
                hashmap[digit] -= 1
        if hashmap[digit] >= 0:
            common = "1"
        else:
            common = "0"
        for row in range(len(nums) - 1, -1, -1):
            if nums[row][digit] != common:
                nums.pop(row)
        digit += 1
    return int(nums[0], 2)

def CO2_ScrubberRating(nums):
    digit = 0
    common = 0

    for i in range(12):
        hashmap[i] = 0
    while len(nums) > 1:
        for row in range(len(nums)):
            nums[row] = nums[row].strip()
            if nums[row][digit] == "1":
                hashmap[digit] += 1
            else:
                hashmap[digit] -= 1
        if hashmap[digit] >= 0:
            uncommon = "0"
        else:
            uncommon = "1"
        for row in range(len(nums) - 1, -1, -1):
            if nums[row][digit] != uncommon:
                nums.pop(row)
        digit += 1
    return int(nums[0], 2)

oxygen_copy = lines[:]
co2_copy = lines[:]
print(oxygenGeneratorRating(oxygen_copy) * CO2_ScrubberRating(co2_copy))