def phoneCall(min1, min2_10, min11, s):
    minutes = 0
    while minutes < 1 and s > min11:
        s = s - min1
        minutes += 1
        print(s, minutes)

    while minutes >= 1 and minutes < 11 and s > min11:
        s = s - min2_10
        minutes += 1
        print(s, minutes)

    while minutes >= 10 and s > min11:
        s = s - min11
        minutes += 1
        print(s, minutes)


    print(minutes)
    return minutes

min1 = 3
min2_10 = 1
min11 = 2
s = 20

phoneCall(min1, min2_10, min11, s)
