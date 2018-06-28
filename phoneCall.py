def phoneCall(min1, min2_10, min11, s):
    minutes = 0
    print(min1, min2_10, min11, s)
    while s > min11:
        while s > min2_10:
            while s > min1 and minutes < 1:
                minutes += 1
                s = s - min1
                print(minutes, s)


min1 = 3
min2_10 = 1
min11 = 2
s = 20

phoneCall(min1, min2_10, min11, s)
