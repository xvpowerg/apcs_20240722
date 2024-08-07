list1 = ['a','b','c']
list2 = ['def','ghij']
print(len(list1))

newList = list1 + list2
print(len(newList))
print(newList)

list1.extend(list2)
print(len(list1))
print(list1)
