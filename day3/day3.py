
file = open('Input.txt', 'r')

text = file.read()

stringsAfterDo = text.split('do()')
stringsWithoutDont = []
stringsSplitByMul = []

for string in stringsAfterDo:
    stringsWithoutDont.append(string.split("don't()")[0])

for string in stringsWithoutDont:
    stringsSplitByMul.append(string.split("mul"))

total = 0


for stringsList in stringsSplitByMul:
    for string in stringsList:
        stringParts = string.split(',')
        try:
            if stringParts[0][0] == '(':
                try:
                    firstNumber = int(stringParts[0][1:])
                except:
                    continue

                try:
                    secondNumber = int(stringParts[1].split(')')[0])
                except:
                    continue

                print(str(firstNumber) + " * " + str(secondNumber))
                total += firstNumber * secondNumber
        except:
            continue

print(total)