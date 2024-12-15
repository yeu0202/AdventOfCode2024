file = open('Input.txt', 'r')

text = file.read()

sections = text.split('\n\n')

rulesSection = sections[0].split('\n')
numbersSection = sections[1].split('\n')

rules = []
numbers = []

correctLines = []
incorrectLines = []
sumOfCorrectLines = 0
sumOfIncorrectLines = 0

def read_rules():
    for rule in rulesSection:
        pair = rule.split('|')
        rules.append([int(pair[0]), int(pair[1])])

def read_numbers():
    for line in numbersSection:
        lines_numbers = line.split(',')
        lines_numbers_int = []
        for number in lines_numbers:
            lines_numbers_int.append(int(number))
        numbers.append(lines_numbers_int)


def is_line_following_rule(line_numbers, rule):
    if not rule[0] in line_numbers or not rule[1] in line_numbers:
        return True
    index_of_first_number = line_numbers.index(rule[0])
    index_of_second_number = line_numbers.index(rule[1])
    if index_of_first_number < index_of_second_number:
        return True
    return False

def is_line_following_rule_swap(line_numbers, rule):
    if not rule[0] in line_numbers or not rule[1] in line_numbers:
        return True
    index_of_first_number = line_numbers.index(rule[0])
    index_of_second_number = line_numbers.index(rule[1])
    if index_of_first_number < index_of_second_number:
        return True
    buffer_number = line_numbers[index_of_first_number]
    line_numbers[index_of_first_number] = line_numbers[index_of_second_number]
    line_numbers[index_of_second_number] = buffer_number
    return True

def fix_wrong_lines():
    for lines in incorrectLines:
        while not is_line_following_all_rules(lines):
            for rule in rules:
                is_line_following_rule_swap(lines, rule)

def is_line_following_all_rules(line_numbers):
    for rule in rules:
        if not is_line_following_rule(line_numbers, rule):
            return False
    return True

def add_correct_lines_to_array():
    for line_numbers in numbers:
        if is_line_following_all_rules(line_numbers):
            correctLines.append(line_numbers)
        else:
            incorrectLines.append(line_numbers)

def add_up_middle_numbers():
    for line_numbers in correctLines:
        global sumOfCorrectLines
        sumOfCorrectLines += line_numbers[int((len(line_numbers) - 1) / 2)]

def add_up_middle_numbers_incorrect():
    for line_numbers in incorrectLines:
        global sumOfIncorrectLines
        sumOfIncorrectLines += line_numbers[int((len(line_numbers) - 1) / 2)]

read_rules()
read_numbers()
add_correct_lines_to_array()
add_up_middle_numbers()
fix_wrong_lines()
add_up_middle_numbers_incorrect()
print(sumOfIncorrectLines)
