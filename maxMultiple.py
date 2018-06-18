def maxMultiple(divisor, bound):
    possibles = 0
    for N in range(0, (bound + 1)):
        print(N)
        if N % divisor == 0 and N <= bound and N > 0:
            possibles = N
            print(possibles)
    return possibles
