pi = 3.14159

def calcArea(r):
    return pi * r * r
def toFahrenheit(tempC):
    return 9 / 5 * tempC + 32
def calcBmi(h,w):
    return w / (h /100) ** 2

def getMessage(bmi):
    if bmi <= 18.5:
        message = "過輕"
    elif 25 > bmi > 18.5:
        message = "正常"
    elif bmi >= 25 and bmi < 30:
        message = "過重"
    elif bmi > 30:
        message = "胖胖"
    return message

print(getMessage(calcBmi(180,70)))
