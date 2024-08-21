myDir = {0:0,1:1}
def fib3(n):
    if n in myDir:
        return myDir[n]
    
    ans1 = fib3(n - 1)
    ans2 = fib3(n - 2)
    result = ans1 + ans2
    myDir[n] = result
    return myDir[n]

print(fib3(6))
