def knapsackLight(value1, weight1, value2, weight2, maxW):
    if weight1 + weight2 <= maxW:
        totalvalue = value1 + value2
    elif value1 > value2 and weight1 <= maxW:
        totalvalue = value1
    elif value2 > value1 and weight2 <= maxW:
        totalvalue = value2
    elif weight1 <= maxW:
        totalvalue = value1
    elif weight2 <= maxW:
        totalvalue = value2
    else:
        totalvalue = 0

    return totalvalue
