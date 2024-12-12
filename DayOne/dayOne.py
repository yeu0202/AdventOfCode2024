listOne = []
listTwo = []
difference = 0

file = open('dayOneInput.txt', 'r')

text = file.read()

splitNumbers = text.split('\n')

for pairs in splitNumbers:
    numbers = pairs.split(' ')
    if len(numbers) < 2:
        break
    firstNumber = int(numbers[0].strip())
    secondNumber = int(numbers[-1].strip())
    listOne.append(firstNumber)
    listTwo.append(secondNumber)

listOne.sort()
listTwo.sort()


def abs_minus(first_number, second_number):
    return abs(first_number - second_number)


differenceList = list(map(abs_minus, listOne, listTwo))


print(sum(differenceList))


similarityScore = 0

for number in listOne:
    appearances = listTwo.count(number)
    similarityScore += appearances * number

print(similarityScore)