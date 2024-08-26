myList = []
# 1 2 3 4 5 6 7 8

#使用迴圈將數值放入myList
for i in range(1,9):
    myList.append(i)
print(myList)    

myList2 = [ i for i in range(1,9)]
print(myList2)

myList3 = [x ** 2 for x in range(1,10)]
print(myList3)
myList4 = [x for x in range(1,10) if x%2 != 0]
print(myList4)
