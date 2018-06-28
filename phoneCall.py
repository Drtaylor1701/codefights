def phoneCall(min1, min2_10, min11, s):
    minutes = 0
    print(min1, min2_10, min11, s)
    while s >= min11 and s > 0:
        while s >= min2_10 and minutes <= 10 and s > 0:
            while s >= min1 and minutes <= 1 and s > 0:
                minutes += 1
                s = s - min1
                print(minutes, s)
            minutes += 1
            s = s - min2_10
            print(minutes, s)
        minutes += 1
        s = s - min11
        print(minutes, s)
    return minutes


min1 = 2
min2_10 = 2
min11 = 1
s = 2

phoneCall(min1, min2_10, min11, s)
