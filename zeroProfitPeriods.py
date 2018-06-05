def zeroProfitPeriods(transactions):
    transaction = 0
    profit = 0
    counter = 0
    for i in transactions:
        print("the entry is " + str(i))
        profit = profit + i
        print("current profit is " + str(profit))
        if profit == 0:
            counter += 1
            print("the current counter is " + str(counter))
    return counter


transactions = [1, 1, 2, -3, 0, 1000, 6, -6, 1, 1, 1, -3, 2]
zeroProfitPeriods(transactions)
