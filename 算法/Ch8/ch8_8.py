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
        
def bin_search(data,val):
    low,high = 0,len(data) - 1
    mid = -1
    while not low > high:
          mid = (low + high) // 2
          if val  < data[mid]:
                high = mid - 1
          elif val > data[mid]:
               low = mid + 1
          else:
              return mid
    return -1
data.sort()
showData(data)
while True:
    val = int(input("請輸入數字(1-100) -1離開"))
    if val == -1:
        break
    pos = bin_search(data,val)
    msg = "找到" if pos > -1 else "找不到"
    print(f"{msg}{val} : {pos}")
