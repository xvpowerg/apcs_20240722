def fib2(n):
    if n ==0 or n == 1:
        return n
    return fib2(n -1 ) + fib2(n - 2)

print(fib2(8))
        
