coinType=(50,10,5,1)

def exchange(amt):
    dp = [amt + 1] *(amt + 1)
    dp[0] = 0
    for i in range(1,amt + 1):
        temp = [dp[i]]
        for coin in coinType:
            if i >= coin:
                temp.append(dp[i - coin] + 1)
        dp[i] = min(temp)
    return -1 if dp[-1]== amt + 1 else dp[-1]
    
amount = int(input("輸入兌換金額:"))
answer = exchange(amount)
print(f"最少需要的硬幣{answer}")

