#2
#3 2 5 6
#7 8 9
c1 = int(input())
myDict = dict()
for i in range(c1):
    tmpList = list(map(int,input().split()))
    countLen = len(tmpList)
    dataList= []
    for i in range(1,countLen):   
        dataList.append(tmpList[i])
    myDict[tmpList[0]]  = dataList  
print(myDict)
