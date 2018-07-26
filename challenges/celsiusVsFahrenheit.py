"""
F = 9 * C / 5 + 32

Your friend lives in Palau (where the Fahrenheit system is used), and you've been trying to find out which of you lives in a warmer climate, so you've each kept track of your respective daily temperatures for the past n days.

Given two arrays of integers yourTemps and friendsTemps (each of length n), representing the local daily temperatures (in Celsius and Fahrenheit, respectively), find how many days were hotter in Palau."""

def celsiusVsFahrenheit(yourTemps, friendsTemps):
    index = 0
    total = 0
    for temp in yourTemps:
        tempInF = 9 * yourTemps[index] / 5 + 32
        if tempInF < friendsTemps[index]:
            total += 1
        index += 1
    return total

yourTemps = [25, 32, 31, 27, 30, 23, 27]
friendsTemps = [78, 83, 86, 88, 86, 89, 79]
celsiusVsFahrenheit(yourTemps, friendsTemps)
