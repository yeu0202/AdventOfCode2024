listOfNumbers = []

file = open('Input.txt', 'r')

text = file.read()

grid = text.split('\n')

xMaxLength = len(grid[0])
yMaxLength = len(grid)

targetWordCount = 0

targetWord = "MAS"
directions = [
    [-1, 0],
    [-1, -1],
    [0, -1],
    [1, -1],
    [1, 0],
    [1, 1],
    [0, 1],
    [-1, 1]
]
diagonalDirections = [
    [-1, -1],
    [-1, 1],
    [1, 1],
    [1, -1]
]

aCountGrid = [[0 for i in range(xMaxLength)] for j in range(yMaxLength)]

def search_for_word(index, direction, letter_in_word):
    xIndex = index[0] + direction[0]
    yIndex = index[1] + direction[1]
    if xIndex < 0 or yIndex < 0  or xIndex > xMaxLength - 1 or yIndex > yMaxLength - 1:
        return
    if grid[xIndex][yIndex] == targetWord[letter_in_word]:
        if letter_in_word == len(targetWord) - 1:
            global targetWordCount
            targetWordCount += 1
        else:
            search_for_word([xIndex, yIndex], direction, letter_in_word + 1)

def search_for_word_starting_with_letter(starting_letter):
    for rowIndex in range(len(grid)):
        for columnIndex in range(len(grid[rowIndex])):
            if grid[rowIndex][columnIndex] == starting_letter:
                for i in range(len(directions)):
                    search_for_word([rowIndex, columnIndex], directions[i], 1)

search_for_word_starting_with_letter(targetWord[0])


partTwoCount = 0

def search_for_word_part_two(index, direction, letter_in_word):
    xIndex = index[0] + direction[0]
    yIndex = index[1] + direction[1]
    if xIndex < 0 or yIndex < 0  or xIndex > xMaxLength - 1 or yIndex > yMaxLength - 1:
        return
    if grid[xIndex][yIndex] == targetWord[letter_in_word]:
        if letter_in_word == len(targetWord) - 1:
            global aCountGrid
            aCountGrid[index[0]][index[1]] += 1
        else:
            search_for_word_part_two([xIndex, yIndex], direction, letter_in_word + 1)

def search_for_x_mas(starting_letter):
    for rowIndex in range(len(grid)):
        for columnIndex in range(len(grid[rowIndex])):
            if grid[rowIndex][columnIndex] == starting_letter:
                for i in range(len(diagonalDirections)):
                    search_for_word_part_two([rowIndex, columnIndex], diagonalDirections[i], 1)

search_for_x_mas(targetWord[0])

for i in range(yMaxLength):
    for j in range(xMaxLength):
        if aCountGrid[i][j] == 2:
            partTwoCount += 1

print(partTwoCount)