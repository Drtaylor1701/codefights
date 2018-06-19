def circleOfNumbers(n, firstNumber):
    if firstNumber != 0 and firstNumber > int(n * .5):
        secondNumber = (n / 2) + firstNumber
    elif firstNumber != 0 and firstNumber < int(n * .5):
        secondNumber = (n / 2) - firstNumber
    else:
        secondNumber = n / 2

    return secondNumber
