def phoneCall(min1, min2_10, min11, s):
    longestCall = 0
    if s < min1:
        print(longestCall)
        return longestCall
    else:
        s = s - min1
        longestCall = 1
        print(longestCall)

    for i in range(2, 11):
        if s < min2_10:
            print(longestCall)
            return longestCall
        else:
            s = s - min2_10
            longestCall += 1
            print(longestCall)

    if s < min11:
        print(longestCall)
        return longestCall
    else:
        while s > min11:
            s = s - min11
            longestCall = longestCall + 1
            print(longestCall)

    print(longestCall)
    return longestCall
