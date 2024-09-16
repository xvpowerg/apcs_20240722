class Item:
    def __init__(self,weight,value):
        self.weight = weight
        self.value = value
def getMaxValue(amt,itemList):
    dp = [0] * (amt + 1)
    dp[0] = 0
    for i in range(1,amt + 1):
        temp = [dp[i]]
        for item in itemList:
            if i >= item.weight:
                temp.append(item.value+dp[i - item.weight])
        dp[i] = max(temp)
    return dp[-1]    
weights = [1,2,3]
values = [20,60,45]
items = []
for w,v in zip(weights,values):
    items.append(Item(w,v))
capacity = 10
maxValue = getMaxValue(capacity,items)
print(f"最大價值:{maxValue}")
