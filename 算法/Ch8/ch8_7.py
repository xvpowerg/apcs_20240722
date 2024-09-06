import random

def showData(data_list):
    for i in range(len(data)//5):
        for j in range(5):
            print('%2d[%3d]  ' %(i*5+j+1,data[i*5+j]),end='')
        print()

val=0
data=[]
while(len(data)<50):
    randNum = random.randint(1,100)
    if(randNum not in data):
        data.append(randNum)
showData(data)
#輸入數字 幫我找這個數字是否在data  在回傳index 不在回傳-1
while True:   
 val = int(input("請輸入(1-100)的數字 -1離開"))
 if val == -1:
     break
 for i in range(50):
     if data[i] == val:
         print(f"找到{val}:{i}")
         break
 else:
     print(f"{val}不存在:-1")
