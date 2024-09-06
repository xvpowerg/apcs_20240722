def showData(data_list):
    for i in range(len(data_list)):
        print(f"{data_list[i]:3}",end="")
    print()     
data=[16,25,39,63,27,12,8,45]
n = len(data)
for i in range(n - 1):
    minIdx = i
    for j in range(i+1,n):
        if data[j] < data[minIdx]:
            minIdx = j
    data[i],data[minIdx] =data[minIdx],data[i]      

showData(data)
