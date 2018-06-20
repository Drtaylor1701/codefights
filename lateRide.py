def lateRide(n):
    tensHours = 0
    hours = 0
    tensMinutes = 0
    minutes = 0
    if n < 60:
        n = str(n)
        tensMinutes = str[0]
        minutes = str[1]
        tensMinutes = int(tensMinutes)
        minutes = int(minutes)
        totalMinutes = tensMinutes + minutes
    elif n >= 60 and n < 600:
        n = n / 60
        n = str(n)
        if len(n) == 1:
            hours = n
            tensMinutes = 0
            minutes = 0
            tensHours = int(tensHours)
            hours = int(hours)
            tensMinutes = int(tensMinutes)
            minutes = int(minutes)
            print("total number of minutes is " + str(totalMinutes))
            return totalMinutes


        totalMinutes = tensHours + hours + tensMinutes + minutes

    print("total number of minutes is " + str(totalMinutes))
    return totalMinutes

n = 240
lateRide(n)
