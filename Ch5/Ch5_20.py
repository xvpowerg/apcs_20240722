num = int(input("請輸入整數:"))
isP = True
for i in range(2,num):
     if num % i == 0:
         isP = False
         break
if  isP:
    print("質數")
else:
    print("不是質數")
