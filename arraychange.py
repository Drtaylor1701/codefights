def arrayChange(inputArray):
    index = 0
    for item in inputArray:
        if index != 0:
            if item != inputArray[index - 1]:
                item += 1
    index += 1
    return inputArray
