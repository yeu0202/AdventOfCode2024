file = open('Input.txt', 'r')

text = file.read()
stringLines = text.split('\n')

possibleOperationsPartOne = [
    '*', '+', '||'
]

equationCollection = []
validEquationCollection = []

def read_input():
    for line in stringLines:
        equation = line.split(':')
        result_answer = int(equation[0])
        component_numbers = equation[1].split(' ')
        component_number_list = []
        for number_index in range(len(component_numbers)):
            if not component_numbers[number_index] == '':
                component_number_list.append(int(component_numbers[number_index]))
        global equationCollection
        equationCollection.append([result_answer, component_number_list])

read_input()

def is_specific_equation_valid(equation_line, possible_operations, operation_list):
    result_number = equation_line[1][0]
    target_number = equation_line[0]
    for operation_index in range(len(operation_list)):
        equation_number_index = operation_index + 1
        operation_string = possible_operations[operation_list[operation_index]]
        if operation_string == '*':
            result_number *= equation_line[1][equation_number_index]
        elif operation_string == '+':
            result_number += equation_line[1][equation_number_index]
        elif operation_string == '||':
            result_number = int(str(result_number) + str(equation_line[1][equation_number_index]))
        else:
            print("invalid operation, please check")
            return False
    if result_number == target_number:
        return True
    return False

def increment_operation_list(operation_list, operation_list_length, possible_operations_length):
    operation_list[0] += 1
    for index in range(operation_list_length):
        if operation_list[index] >= possible_operations_length:
            operation_list[index] = 0
            operation_list[index + 1] += 1
    return operation_list

def is_equation_valid(equation_line, possible_operations):
    operation_list_length = len(equation_line[1]) - 1
    operation_list = [0 for _ in range(operation_list_length)]
    last_possible_operations = [len(possible_operations) - 1 for _ in range(operation_list_length)]
    while operation_list != last_possible_operations:
        if is_specific_equation_valid(equation_line, possible_operations, operation_list):
            return True
        operation_list = increment_operation_list(operation_list, operation_list_length, len(possible_operations))
    # need to check last possible operations
    if is_specific_equation_valid(equation_line, possible_operations, operation_list):
        return True
    return False

def find_valid_equations_part_one(equation_collection, valid_equation_collection, possible_operations):
    for equation_line in equation_collection:
        if is_equation_valid(equation_line, possible_operations):
            valid_equation_collection.append(equation_line)

def count_total_result(valid_equation_collection):
    total = 0
    for equation_line in valid_equation_collection:
        total += equation_line[0]
    return total

find_valid_equations_part_one(equationCollection, validEquationCollection, possibleOperationsPartOne)
validEquationsTotal = count_total_result(validEquationCollection)
print(validEquationsTotal)