def phoneCall(min1, min2_10, min11, s):
    longestCall = 0
    if s > min1:
        longestCall = 1
        s = s - min1
    else:
        print(s, longestCall)
        return longestCall

    for i in range(2, 11):
        if s > min2 * i:
            print(s, longestCall)
        longestCall = longestCall + i
        s = s - (min2 * i)
        print(s, longestCall)
        return longestCall

    print(s, longestCall)
    return longestCall
