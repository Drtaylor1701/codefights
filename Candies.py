def candies(n, m):
    candiesEatenPerChild = m % n
    print(candiesEatenPerChild)
    return candiesEatenPerChild

children = 3
candy = 9
candies(children, candy)
