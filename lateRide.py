def lateRide(n):
    if n % 60 == 0:
        hours = n / 60
        hours = str(hours)
        print(hours)
        lengthofHours = len(int(hours))
        print(lengthofHours)
n = 240
lateRide(n)
