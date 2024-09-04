"""
組合

想法:
1, 2, 3, 4, 5  取3 不知道多少 但我可以算

1 合併 2 3 4 5取2的組合

我不知道2 3 4 5取2的組合 多少

但我可以算

2 合併 3 4 5 取1的組合 

"""
def combine(lst,n):
    if len(lst) == n:
        return [lst]
    elif n == 1:
        return [[x] for x in lst]
    else:
        out = []
        for i in range(len(lst) - n + 1):
                for c in combine(lst[i+1:],n-1):
                   out.append([lst[i]] + c)
        return out           
myList = combine([1,2,3,4,5,6],4)
for i in myList:
    print(i)
