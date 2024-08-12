from calculator import calcBmi,getMessage
h = int(input("身高"))
w = int(input("體重"))
bmi = calcBmi(h,w)
msg = getMessage(bmi)
print(bmi,msg)
