def knapsackLight(value1, weight1, value2, weight2, maxW):
    if weight1 + weight2 <= maxW:
        totalValue = value1 + value2
    else:
        if weight1 > maxW and weight2 > maxW:
            totalValue = 0
        elif weight1 > weight2:
            totalValue = value1
        else:
            totalValue = value2

    return totalValue
