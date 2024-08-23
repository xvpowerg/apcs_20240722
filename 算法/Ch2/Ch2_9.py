a1 =int(input("輸入首項"))
d = int(input("輸入公差"))
n = int(input("輸入項數"))
sum1 = 0
for i in range(n):
    ai = a1 + i * d    
    sum1 += ai
    print(ai,end="\t")
print("=>sum:",sum1)
