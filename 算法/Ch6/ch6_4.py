from  math import sqrt
n = 72
print(f"{n}=",end="")

while True:
    for i in range(2,int(sqrt(n)) + 1):
        if n % i == 0:
            n = int(n / i)
            print(f"{i}*",end="")
            break
    else:
        print(n)
        break
