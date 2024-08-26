values = input("輸入一群整數用空白隔開")
arr = list(map(int,values.split()))
num = len(arr)
for i in  range(num-1):
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
