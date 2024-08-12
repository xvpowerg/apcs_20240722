import random
ans = random.randint(1,5)#包含到5
guess = int(input("請輸入一個1~5的數字:"))

if guess == ans:
    print("猜對了")
else:
    print("猜錯了,答案是:",ans)

