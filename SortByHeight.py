def sortByHeight(a):
    sortingArray = []
    for number in a:
        if number != -1:
            sortingArray.append(number)
            print(sortingArray)

    sortedHeights = sorted(sortingArray)
    print(sortedHeights)
    aIndex = 0
    sortedHeightsIndex = 0
    for item in sortedHeights:
        if a[aIndex] != -1:
            a[aIndex] = item
        aIndex += 1

    return a

a = [-1, 150, 190, 170, -1, -1, 160, 180]
