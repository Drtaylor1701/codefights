def isLucky(n):
    n = str(n)
    print(n)
    lengthOfN = len(n)
    firsthalfIndex = int((lengthOfN / 2))
    secondhalfIndex = int(lengthOfN / 2)
    print(firsthalfIndex)
    print(secondhalfIndex)
    firstHalf = n[:firsthalfIndex]
    print(firstHalf)
    secondHalf = n[secondhalfIndex:]
    print(secondHalf)
    sumoffirsthalf = 0
    sumofsecondhalf = 0
    for number in firstHalf:
        number = int(number)
        sumoffirsthalf = sumoffirsthalf + number
        print("The first half sum is: " + str(sumoffirsthalf))

    for number in secondHalf:
        number = int(number)
        sumofsecondhalf = sumofsecondhalf + number
        print("The second half sum is: " + str(sumofsecondhalf))

    if sumoffirsthalf == sumofsecondhalf:
        return True
    else:
        return False

n = 1230
isLucky(n)
