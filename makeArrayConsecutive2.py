def makeArrayConsecutive2(statues):
    print("started test")
    statues = sorted(statues)
    print(statues)
    maxArray = statues[len(statues) - 1]
    print(maxArray)
    count = statues[0]
    extraStatues = 0

    while count <= maxArray:
        print(count, extraStatues)
        if count not in statues:
            print("if statement triggered")
            extraStatues += 1
        count += 1
        print("while loop ran")
        print(count, extraStatues)
    return extraStatues

test1 = [6, 2, 3, 8]
test2 = [0, 3]
test3 = [5, 4, 6]
test4 = [6, 3]
test5 = [1]
makeArrayConsecutive2(test1)
#makeArrayConsecutive2(test2)
#makeArrayConsecutive2(test3)
#makeArrayConsecutive2(test4)
#makeArrayConsecutive2(test5)
