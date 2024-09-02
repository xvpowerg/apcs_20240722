import math
n = 10
primeList = []
def is_prime(num):
    for i in range(2,int(math.sqrt(num)) + 1):
            if num % i == 0 :
                return False
    return True

for i in range(1,n + 1):
    if is_prime(i):
        primeList.append(i)
print(primeList)        
        
