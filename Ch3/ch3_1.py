h = float(input("身高,單位為公分:"))
w = int(input("體重,單位為公斤:"))
bmi = w / ((h/100) ** 2)
print("bmi:%.2f"%(bmi))
print(f"bmi:{bmi:.2f}")
bmif = bmi
print(type(bmif),round(bmif,2))
