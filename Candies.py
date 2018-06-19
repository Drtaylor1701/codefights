def candies(n, m):
    if m % n == 0:
        candiesPerChild = m / n
    else:
        candiesPerChild = m / n
        candiesPerChild = int(candiesPerChild)
    print(candiesPerChild)
    candiesEaten = candiesPerChild * n
    print(candiesEaten)
    return candiesEaten

children = 3
candy = 9
candies(children, candy)
