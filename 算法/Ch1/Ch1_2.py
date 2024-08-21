def f2(n):
    if n == 1:
        return 1
    else:
        return f2(n-1) * n

def f1(n):
    ans = 1
    for i in range(1,n+1):
        ans *= i
    return ans
print(f1(5))
print(f2(5))
