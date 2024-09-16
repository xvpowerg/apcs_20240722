import sys
bottleType = (30,18,5,1)
def exchange(amt):
    global count
    result = {}
    for bottle in bottleType:
        num = amt // bottle
        result[bottle] = num
        count += num
        amt %= bottle
    return result

print("輸入水量:",end="")
amount = int(sys.stdin.readline())
count = 0  
ans = exchange(amount)
for bottle in bottleType:
    print(f"{bottle}公升容量{ans[bottle]}個")
print(f"共使用{count}個容器")

  
