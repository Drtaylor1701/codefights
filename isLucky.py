def isLucky(n):
    halflengthofn == len(n)/2
    nasstring = str(n)
    firsthalf = nasstring[0:halflengthofn - 1]
    secondhalf = [halflengthofn:]
    print(firsthalf, secondhalf)
    firsthalftotal = 0
    secondhalftotal = 0
    for number in firsthalf:
        number = int(number)
        firsthalftotal == firsthalftotal + number

    for number in secondhalf:
        number = int(number)
        secondhalftotal = secondhalftotal + number

    if firsthalftotal == secondhalftotal:
        return true
    else:
        return false
        
