def sortByHeight(a):
    sortingArray = []
    indexes = []
    newArray = []
    for index in range(0, len(a)):
        if a[index] == -1:
            print("the index is " + str(index))
            indexes.append(index)

    print("The -1s are positioned at " + str(indexes))

    index = 0
    for index in range(0, len(a)):
        if a[index] != -1:
            sortingArray.append(a[index])
    sortingArray = sorted(sortingArray)
    print("The sorted list of heights is " + str(sortingArray))

    index = 0
    sortedindex = 0
    for index in range(0, len(a)):
        if index in indexes:
            a[index] = -1
            print("currently, the array is " + str(a))
        else:
            a[index] = sortingArray[sortedindex]
            sortedindex += 1
            print("currently, the array is " + str(a))
        index += 1
        print(index)
        print(sortedindex)
    return a


a = [-1, 150, 190, 170, -1, -1, 160, 180]
sortByHeight(a)
