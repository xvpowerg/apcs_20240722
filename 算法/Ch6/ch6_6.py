def myLog(a,b,pre=2):
    step = 1
    ans = step
    while (step >= 10**-pre):
        while (b ** ans < a):
            ans += step
            if (b ** ans == a):
                return ans
        ans -= step
        step /= 10
    return ans
a = 25
b = 2
print(f"{myLog(a,b,6):.6}")
