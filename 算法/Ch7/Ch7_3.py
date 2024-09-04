numberList = []
def permute2(n,end):
    if n == end:
        print(numberList)       
    else:
        for i in range(1,end+1):
            if i not in numberList:
               numberList.append(i)
               permute2(n + 1,end)
               numberList.pop()
permute2(0,4)

