myStr1 = "12 15 16 17 18"
myList =  myStr1.split()
mapObj = map(int,myList)
intList =  list(mapObj)

mySum = 0

for v in intList:
    mySum += v
print(mySum)    

