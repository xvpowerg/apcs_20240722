import random

lottoNums = random.sample(range(1,50),6)
speciaNum = random.randint(1,49)
while speciaNum in lottoNums:
    speciaNum = random.randint(1,49)
print("樂透號:",lottoNums)
print("特別號:",speciaNum)    
