def lateRide(n):
    #first, I'll need to convert the number to a string
    n = str(n)
    print("the total number of minutes is " + n)
    #next, I'll need to separate the digits, so I'll have to convert them to
    #strings and go through them one at a time
    if len(n) == 4:
        n1 = n[0]
        n2 = n[1]
        n3 = n[2]
        n4 = n[3]
    elif len(n) == 3:
        n1 = n[0]
        n2 = n[1]
        n3 = n[2]
        n4 = 0
    elif len(n) == 2:
        n1 = n[0]
        n2 = n[1]
        n3 = 0
        n4 = 0
    else:
        total = n[0]
        return total

    print(n1, n2, n3, n4)
    #then I'll need to convert each digit back to int or float and add them
    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)
    n4 = int(n4)
    total = n1 + n2 + n3 + n4
    #return the total
    print(total)
    return total
    #also, this is a silly way to do anything and nobody would do this

    #especially on a freaking motorcycle


n = 240
lateRide(n)
