def isInfiniteProcess(a, b):
    if (b - a) % 2 != 0 or b - a < 0:
        return True
    else:
        return False
