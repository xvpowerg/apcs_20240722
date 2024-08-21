def fib_for(n):
    if n == 0 or n == 1:
        return n
    num1,num2 = 0,1
    nextNum = num1 + num2
    for i in range(2,n):
        num1 = num2
        num2 = nextNum
        nextNum = num1 + num2
    return nextNum

print(fib_for(8))
