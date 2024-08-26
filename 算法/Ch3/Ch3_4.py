def printData(x):
    for i in range(len(x)):
        print(x[i],end="")
        if i < len(x) - 1:
            print(end=" ")
    
x = [5, 15, 25, 35, 45]
for data in x:
    print(data,end = ",")
print()
printData(x)
x.insert(2,100)
print()
printData(x)
x[2] = 20
print()
printData(x)
print()
x.remove(20)
printData(x)
print()
n = x.pop()
print(n)
printData(x)
n = x.pop(2)
print()
print(n)
printData(x)
