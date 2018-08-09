def tennisSet(score1, score2):
    if score1 == 6 and score2 < 5:
        return True
    elif score2 == 6 and score1 < 5:
        return True
    elif score1 == score2:
        return False
    elif score1 >= 5 and score2 == 7:
        return True
    elif score2 >= 5 and score1 == 7:
        return True
    else:
        return False
