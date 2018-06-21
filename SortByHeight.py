def sortByHeight(a):
    sortingArray = []
    indexes = []
    newArray = []
    for index in range(0, len(a)):
        if a[index] == -1:
            print(index)
            indexes.append(index)

    print(indexes)

    index = 0
    for index in range(0, len(a)):
        if a[index] != -1:
            sortingArray.append(a[index])
    sortingArray = sorted(sortingArray)
    print(sortingArray)

    index = 0
    sortedindex = 0
    for index in range(0, len(a)):
        if index in indexes:
            a[index] = -1
        else:
            a[index] = sortingArray[sortedindex]
            sortedindex += 1
        index += 1
        print(a)


a = [-1, 150, 190, 170, -1, -1, 160, 180]
sortByHeight(a)
