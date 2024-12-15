import copy

listOfNumbers = []

file = open('Input.txt', 'r')

text = file.read()

splitNumbers = text.split('\n')

def cast_int(input_num):
    return int(input_num)


def number_are_safe(report_numbers, increasing):
    for number in range(len(report_numbers) - 1):
        first_number = report_numbers[number]
        second_number = report_numbers[number + 1]
        if increasing:
            difference = second_number - first_number
        else:
            difference = first_number - second_number
        if difference > 3 or difference < 1:
            return False
    return True

def number_are_safe_dampening(report_numbers, increasing):
    for number in range(len(report_numbers) - 1):
        first_number = report_numbers[number]
        second_number = report_numbers[number + 1]
        if increasing:
            difference = second_number - first_number
        else:
            difference = first_number - second_number
        if difference > 3 or difference < 1:
            list_one = copy.deepcopy(report_numbers)
            list_two = copy.deepcopy(report_numbers)
            list_one.pop(number)
            list_two.pop(number + 1)
            return number_are_safe(list_one, increasing) or number_are_safe(list_two, increasing)
    return True


for pairs in splitNumbers:
    numbers = pairs.split(' ')
    if len(numbers) < 2:
        break
    listOfNumbers.append(list(map(cast_int, numbers)))

count2 = 1
safeCount = 0
for report in listOfNumbers:
    increasingSafe =  number_are_safe_dampening(report, True)
    decreasingSafe = number_are_safe_dampening(report, False)
    if increasingSafe or decreasingSafe:
        safeCount+=1
    print("count: " + str(count2) + " safe: " + str(safeCount))
    count2 += 1

count = 1
safeCountOne = 0
for report in listOfNumbers:
    increasingSafe =  number_are_safe(report, True)
    decreasingSafe = number_are_safe(report, False)
    if increasingSafe or decreasingSafe:
        safeCountOne+=1
    # print("count: " + str(count) + " safe: " + str(safeCountOne))
    count += 1

print(safeCount)