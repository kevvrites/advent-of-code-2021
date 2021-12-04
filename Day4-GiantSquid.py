# Given bingo drawings and boards
f = open("Day4-Input.txt")
lines = f.readlines()

# 
drawings = lines[0].strip().split(',')
lines.pop(0)
boards = []

for line in range(len(lines)):
    lines[line] = lines[line].strip()

while len(lines) > 0:
    lines.pop(0)

    for i in range(5):
        if len(lines) != 0:
            boards.append(lines.pop(0))

boards = " ".join(boards)
boards = boards.split()  

# Board is one array of 25 characters
# Diagonals don't count as wins
def checkWinningBoard(board, drawings, max_drawings):
    winning_index = set()
    # Vertical Wins
    vertwin1 = {0, 5, 10, 15, 20}
    vertwin2 = {1, 6, 11, 16, 21}
    vertwin3 = {2, 7, 12, 17, 22}
    vertwin4 = {3, 8, 13, 18, 23}
    vertwin5 = {4, 9, 14, 19, 24}

    # Horizontal wins
    horizwin1 = {0, 1, 2, 3, 4}
    horizwin2 = {5, 6, 7, 8, 9}
    horizwin3 = {10, 11, 12, 13, 14}
    horizwin4 = {15, 16, 17, 18, 19}
    horizwin5 = {20, 21, 22, 23, 24}

    # Diagonal wins
    #diagwin1 = {0, 6, 12, 18, 24}
    #diagwin2 = {4, 8, 12, 16, 20}

    winning_sets = [vertwin1, vertwin2, vertwin3, vertwin4, vertwin5, horizwin1, horizwin2, horizwin3, horizwin4, horizwin5, ]#diagwin1, diagwin2]
    win = False
    for drawing in range(max_drawings):
        if win == True:
            break
        if drawings[drawing] in board:
            found = board.index(drawings[drawing])
            winning_index.add(found)
        if len(winning_index) >= 5:
            for win in winning_sets:
                if win.issubset(winning_index):
                    win = True
                    drawing_win = drawing
                    break
    if win == True:
        return drawing_win
    else:
        return -1

boards_wins = {}

for idx in range(0, len(boards) // 25):
    board = boards[idx * 25: idx*25 + 25]
    res = checkWinningBoard(board, drawings, len(drawings))
    boards_wins[idx] = res

def scoreWinningBoard(board_index, drawing_count):
    board = boards[board_index * 25: board_index * 25 + 25]
    sum = 0
    for drawing in range(drawing_count + 1):
        if drawings[drawing] in board:
            board.remove(drawings[drawing])
    for num in board:
        sum += int(num)
    score = sum * int(drawings[drawing_count])
    return score

# Find the first winning board and return score
firstWin = min(boards_wins.items(), key=lambda x: x[1])
print(scoreWinningBoard(firstWin[0], firstWin[1]))


# PART 2
# Find the last winning board and return score
lastWin = max(boards_wins.items(), key=lambda x: x[1])
print(scoreWinningBoard(lastWin[0], lastWin[1]))