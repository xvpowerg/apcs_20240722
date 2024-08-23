a1 =int( input("輸入首項"))
d = int(input("輸入公差"))
n = int(input("輸入項數"))


def getAn(n):
    if n == 1:
        return a1
    else:
        return getAn(n - 1) + d

print(getAn(n))
