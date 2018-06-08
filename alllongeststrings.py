def allLongestStrings(inputArray):
    print(inputArray)
    greatest = 0
    allstrings = []
    for string in inputArray:
        if len(string) > greatest:
            greatest = len(string)
        print(greatest)
    for item in inputArray:
        if len(item) == greatest:
            allstrings.append(item)
    print(allstrings)
    return allstrings



inputArray=["aba", "aa", "ad", "vcd", "aba"]
allLongestStrings(inputArray)
