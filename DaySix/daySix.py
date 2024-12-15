import copy

file = open('Input.txt', 'r')

text = file.read()
stringArray = text.split('\n')
xMaxLength = len(stringArray[0])
yMaxLength = len(stringArray)

grid = [['A' for i in range(xMaxLength)] for j in range(yMaxLength)]
for yCoord in range(yMaxLength):
    for xCoord in range(xMaxLength):
        grid[yCoord][xCoord] = stringArray[yCoord][xCoord]


walkedPath = [['0' for i in range(xMaxLength)] for j in range(yMaxLength)]

directions = [
    [-1,0],
    [0, 1],
    [1, 0],
    [0, -1]
]

guardPos = [0, 0]
directionValue = 0

def find_guard(initial_grid, walked_path):
    for y_index in range(yMaxLength):
        for x_index in range(xMaxLength):
            if initial_grid[y_index][x_index] == '^':
                global guardPos
                guardPos = [y_index, x_index]
                mark_guard_pos(walked_path)

def mark_guard_pos(walked_path):
    walked_path[guardPos[0]][guardPos[1]] = 'X'

def move_guard(initial_grid):
    global guardPos
    global directionValue
    next_index_y = guardPos[0] + directions[directionValue][0]
    next_index_x = guardPos[1] + directions[directionValue][1]
    if next_index_x > xMaxLength - 1 or next_index_x < 0 or next_index_y > yMaxLength - 1 or next_index_y < 0:
        return True
    if initial_grid[next_index_y][next_index_x] != '#':
        guardPos = [next_index_y, next_index_x]
        return False
    else:
        directionValue += 1
        directionValue = directionValue % 4
        return False

def move_guard_all(initial_grid, walked_path):
    while not move_guard(initial_grid):
        mark_guard_pos(walked_path)

def count_xes(walked_path):
    walked_squares_count = 0
    for line in walked_path:
        walked_squares_count += line.count('X')
    return walked_squares_count

find_guard(grid, walkedPath)
initialGuardPos = copy.deepcopy(guardPos)

move_guard_all(grid, walkedPath)
walkedSquaresCount = count_xes(walkedPath)
print(walkedSquaresCount)


loopLocations = [['.' for k in range(xMaxLength)] for l in range(yMaxLength)]
max_steps_allowed = xMaxLength * yMaxLength * 2

def find_looping_areas():
    for y_coord in range(yMaxLength):
        for x_coord in range(xMaxLength):
            if y_coord == initialGuardPos[0] and x_coord == initialGuardPos[1]:
                continue
            if walkedPath[y_coord][x_coord] == 'X':
                temp_board = copy.deepcopy(grid)
                temp_board[y_coord][x_coord] = '#'
                temp_walked_path = [[0 for _ in range(xMaxLength)] for _ in range(yMaxLength)]

                steps_taken = 0
                global directionValue
                global guardPos
                directionValue = 0
                guardPos = initialGuardPos
                while not move_guard(temp_board):
                    mark_guard_pos(temp_walked_path)
                    steps_taken += 1
                    if steps_taken > max_steps_allowed:
                        loopLocations[y_coord][x_coord] = 'X'
                        break

find_looping_areas()
# Warning: gets exponentially slow
loopLocationsCount = count_xes(loopLocations)
print(loopLocationsCount)
