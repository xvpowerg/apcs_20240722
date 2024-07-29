str1 = "ABCDEF"
#左往右正數由0開始
print(str1[2])
#右往左負數由-1開始
print(str1[-2])
print(str1[:4])
print(str1[1:])
print(str1[1:4])
print(str1[-4:-1])
print(str1[::-1])
print(str1[-3:0:-1])
print(str1[::2])
#str1 時間複雜度O(n)
str2 = str1[1:4]
print(str2)
