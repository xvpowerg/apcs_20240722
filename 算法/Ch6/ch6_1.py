def isPrime(number):
    for i in range(2,number):
        if number % i == 0:
            return False
    return True

n = 10
primeNums = []
for j in range(2,n+1):
    if isPrime(j):
        primeNums.append(j)
        
print(f"小於等於{n}的質數:",primeNums)
