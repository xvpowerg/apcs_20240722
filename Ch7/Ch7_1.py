def calcBMI(h,w):
    return w / ((h/100)**2)
def testBmi(bmi):
    result="錯誤"
    if bmi > 30:
        result= "胖胖"
    elif bmi > 25:
        result = "過重"
    elif bmi > 18.5:
        result = "正常"
    elif bmi > 0:
        result = "過輕"
    return result

h = float(input("請輸入身高"))
w = int(input("請輸入體重"))
bmi = calcBMI(h,w)
print(f"{bmi:.2f}",testBmi(bmi))
