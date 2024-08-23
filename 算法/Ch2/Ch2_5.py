a1 =int( input("輸入首項"))
r = int(input("輸入公比"))
n = int(input("輸入項數"))
for i in range(n):
    print(a1 * r ** i ,end = '\t')

