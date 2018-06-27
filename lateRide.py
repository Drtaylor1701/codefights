def lateRide(n):
    hours = 0
    minutes = 0
    total = 0
    while n >= 60:
        hours = hours + 1
        n = n - 60
        print("the total numbers of hours and current value of n is " + str(hours), str(n))

    hours = int(hours)
    print(hours)

    minutes = n

    hours = str(hours)
    minutes = str(minutes)
    time = str(hours+":"+minutes)
    print(time)

    for character in time:
        if character != ":":
            print(character)
            character = int(character)
            total = total + character
    print(total)
    return total

n = 240
lateRide(n)
n = 808
lateRide(n)
