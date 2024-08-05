def myFun1(x):
    return x * 2
myList = [5,6,7,8]
mapObj = map(myFun1,myList)
print(list(mapObj))
