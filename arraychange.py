def arrayChange(inputArray):
    index = -1
    changecount = 0
    for item in inputArray:
        if index == -1:
            index += 1
        while item != (inputArray[index] + 1):
            inputArray[index + 1] = item + 1
            changecount += 1
    return changecount
