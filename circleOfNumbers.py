def circleOfNumbers(n, firstNumber):
    if firstNumber != 0 and firstNumber > (n / 2):
        secondNumber = (n / 2) - firstNumber
    elif firstNumber != 0 and firstNumber < (n / 2):
        secondNumber = (n / 2) + firstNumber
    elif firstNumber == (n / 2):
        secondNumber = 0
    else:
        secondNumber = n / 2

    if secondNumber < 0:
        secondNumber = secondNumber * -1

    print(secondNumber)
    return secondNumber

n = 10
firstNumber = 7
circleOfNumbers(n, firstNumber)
