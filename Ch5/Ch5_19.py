results = {"David":1, "Amy":2, "Sean":1}
sortList = []
for key,value in results.items():
    sortList.append((key,value))

maxTuple = ()
myMax = 0
for n,c in sortList:
     if c > myMax:
         myMax = c
         maxTuple = (n,c)

print(maxTuple)
