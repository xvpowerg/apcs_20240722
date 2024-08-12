import random
def mySample(data,count):
    myLen = len(data)
    result = []
    if count >= myLen:
        return data
    indexSet = set()
    while True:
        index = random.randint(1,myLen) - 1
        indexSet.add(index)
        if len(indexSet) == count:
            break
    for i in  indexSet:
        result.append(data[i])
    return result
fruits = ['香蕉', '蘋果', '橘子', '西瓜']
ans = mySample(fruits,2)
print(ans)
