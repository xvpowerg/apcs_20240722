sum1 = 0
for i in range(1,6):
    sum1 += 2 * i *(3*i+1)
print(sum1)    

def simgaSum(n):
    if n == 1:
        return 2 * n*(3*n + 1)
    else:
        return simgaSum(n-1) + 2 * n*(3*n + 1)
    
print(simgaSum(5))
