arr =  [[0] * 6 for row in range(6)]
print(arr)

data=[[1,2],[2,1],[1,5],[5,1],              #圖形各邊的起點值及終點值
      [2,3],[3,2],[2,4],[4,2],
      [3,4],[4,3]]

for i in range(10):
    tmpi = data[i][0]
    tmpj = data[i][1]
    arr[tmpi][tmpj] = 1
    
for i in range(1,6):
    for j in range(1,6):
        print(f"[{arr[i][j]}]",end="")
    print()    
