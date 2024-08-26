n = int(input("輸入n"))
sum1 = 0

def getSum(n):
    if n == 1 or n == 0:
        return 0
    else:
        return getSum(n - 1) + (n - 1) * n

print(getSum(n))
