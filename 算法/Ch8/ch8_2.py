def showData(data_list):
    for i in range(len(data_list)):
        print(f"{data_list[i]:3}",end="")
    print()     
data=[16,25,39,63,27,12,8,45]
showData(data)
n = len(data)
print(n)
for i in range(1,n):
    for j in range(n-i):
        if data[j] > data[j + 1]:
            data[j],data[j + 1] = data[j + 1],data[j]

showData(data)            
