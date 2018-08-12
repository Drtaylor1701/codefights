def areSimilar(a, b):
    print(a, b)
    if a == b:
        return True

    for number in a:
        if number not in b:
            return False

    a = a.sort()
    b = b.sort()
    print(a, b)

    return True


a = [1, 2, 3]
b = [2, 1, 3]
areSimilar(a, b)
