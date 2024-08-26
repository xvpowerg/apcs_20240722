num = int(input("輸入陣列個數:"))
arr = [0]*num

for i in range(num):
    arr[i] = int(input("輸入整數:"))

for i in  range(num - 1):
    if arr[i] >= arr[i+1]:
        print("不是遞增矩陣")
        break
else:
    print("遞增矩陣")

for i in range(num - 1):
    if arr[i] * arr[i + 1] >= 0:
        print("不是正負交錯")
        break
else:
    print("正負交錯")

