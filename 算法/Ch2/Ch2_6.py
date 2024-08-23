a1 =int( input("輸入首項"))
r = int(input("輸入公比"))
n = int(input("輸入項數"))

def getAn(n):
    if n == 1:
        return a1
    else:
        return getAn(n-1) * r
print(getAn(n))    
