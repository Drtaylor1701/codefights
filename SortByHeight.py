def sortByHeight(a):
    sortingArray = []
    indexes = []
    for index in range(0, len(a)):
        if a[index] == -1:
            print(index)
            indexes.append(index)

    print(indexes)

    while a != -1:
        sortingArray.append(a)
        print(sortingArray)

a = [-1, 150, 190, 170, -1, -1, 160, 180]
sortByHeight(a)
