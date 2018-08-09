def willYou(young, beautiful, loved):
    if (young == True and beautiful == True and loved == True) or (young == False and beautiful == False and loved == False) or (young == False and beautiful == True and loved == False) or (young == True and beautiful == False and loved == False):
        return False
    elif (young == True and beautiful == True and loved == False) or (young == True and beautiful == False and loved == True) or (young == False and beautiful == True and loved == True) or (young == False and beautiful == False and loved == True):
        return True
