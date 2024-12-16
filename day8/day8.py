import copy

file = open('Input.txt', 'r')

text = file.read()
stringArray = text.split('\n')
xMaxLength = len(stringArray[0])
yMaxLength = len(stringArray)

grid = [['.' for i in range(xMaxLength)] for j in range(yMaxLength)]
for yCoord in range(yMaxLength):
    for xCoord in range(xMaxLength):
        grid[yCoord][xCoord] = stringArray[yCoord][xCoord]

antennaPositionsPerType = []
antiNodePositionsPerType = []


#                                                 'A' or '0' etc
def find_grid_for_antenna_type(grids_per_antenna, antenna_type):
    for antenna_entry in grids_per_antenna:
        if antenna_entry[0] == antenna_type:
            return antenna_entry
    return None


def separate_grid_into_antennas(initial_grid, antenna_positions_per_type):
    for y_index in range(yMaxLength):
        for x_index in range(xMaxLength):
            antenna_type = initial_grid[y_index][x_index]
            if antenna_type != '.':
                antenna_entry = find_grid_for_antenna_type(antenna_positions_per_type, antenna_type)
                if antenna_entry is None:
                    antenna_entry = [antenna_type, []]
                    antennaPositionsPerType.append(antenna_entry)
                antenna_entry[1].append([y_index, x_index])


def find_anti_nodes_from_positions(node_type_with_positions, anti_node_positions):
    for node_index in range(len(node_type_with_positions[1]) - 1):
        for second_node_index in range(node_index + 1, len(node_type_with_positions[1])):
            node_one_pos = node_type_with_positions[1][node_index]
            node_two_pos = node_type_with_positions[1][second_node_index]
            difference = [node_two_pos[0] - node_one_pos[0], node_two_pos[1] - node_one_pos[1]]
            multiplier_index = 0
            while True:
                anti_node = [node_one_pos[0] - difference[0] * multiplier_index, node_one_pos[1] - difference[1] * multiplier_index]
                if -1 < anti_node[0] < yMaxLength and -1 < anti_node[1] < xMaxLength:
                    anti_node_positions.add(tuple(anti_node))
                    multiplier_index += 1
                else:
                    break
            multiplier_index = 0
            while True:
                anti_node = [node_one_pos[0] - difference[0] * multiplier_index, node_one_pos[1] - difference[1] * multiplier_index]
                if -1 < anti_node[0] < yMaxLength and -1 < anti_node[1] < xMaxLength:
                    anti_node_positions.add(tuple(anti_node))
                    multiplier_index -= 1
                else:
                    break


def find_anti_nodes(antenna_positions_per_type, anti_node_positions_per_type):
    for node_type_with_positions in antenna_positions_per_type:
        anti_node_positions = set()
        anti_node_positions_per_type.append([node_type_with_positions[0], anti_node_positions])
        find_anti_nodes_from_positions(node_type_with_positions, anti_node_positions)


def count_anti_nodes(anti_node_positions_per_type):
    total_count = 0
    for anti_node_positions in anti_node_positions_per_type:
        total_count += len(anti_node_positions[1])
    return total_count

separate_grid_into_antennas(grid, antennaPositionsPerType)
find_anti_nodes(antennaPositionsPerType, antiNodePositionsPerType)
antiNodeCount = count_anti_nodes(antiNodePositionsPerType)

def show_anti_node_positions(initial_grid, anti_node_positions_per_type):
    duplicate_grid = copy.deepcopy(initial_grid)
    for anti_node_positions in anti_node_positions_per_type:
        for node_positions in anti_node_positions[1]:
            duplicate_grid[node_positions[0]][node_positions[1]] = '#'
    for row in duplicate_grid:
        print(row)
    return duplicate_grid

duplicateGrid = show_anti_node_positions(grid, antiNodePositionsPerType)
print(antiNodeCount)

def consolidate_anti_node_positions(anti_node_positions_per_type):
    anti_node_collection = set()
    for node_positions_per_type in anti_node_positions_per_type:
        for node in node_positions_per_type[1]:
            anti_node_collection.add(tuple(node))
    return anti_node_collection

consolidatedAntiNodePositions = consolidate_anti_node_positions(antiNodePositionsPerType)
print(len(consolidatedAntiNodePositions))
