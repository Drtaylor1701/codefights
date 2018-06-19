def zeroProfitPeriods(transactions):
    transaction = 0
    counter = 0
    profitTracker = 0
    lengthOfTransactions = len(transactions)
    while transaction <= (lengthOfTransactions - 1):
        profit = 0
        for item in transactions:
            if item + profit == 0:
                counter += 1
            else:
                profit = item + profit
            transaction += 1

    print(counter)
    return counter


transactions = [1, 1, 2, -3, 0, 1000, 6, -6, 1, 1, 1, -3, 2]
zeroProfitPeriods(transactions)
