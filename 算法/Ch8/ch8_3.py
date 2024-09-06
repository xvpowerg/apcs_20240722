def showData(data_list):
    for i in range(len(data_list)):
        print(f"{data_list[i]}",end=" ")
    print()     
#字典序 小寫 > 大寫 > 數字  
cars=["Audi", "Honda", "Mazda", "Ford", "Benz", "Lexus", "BMW"]
showData(cars)
n = len(cars)

for i in range(1,n):
    for j in range(n - i):
        if cars[j] > cars[j+1]:
            cars[j],cars[j + 1] = cars[j + 1],cars[j]
            
showData(cars)
