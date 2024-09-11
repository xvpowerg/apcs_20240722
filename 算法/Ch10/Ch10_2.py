arr = [[0] * 6 for row in range(6)]

data=[[1,2],[2,1],[2,3],[2,4],[4,3],[4,1]]  
for i in range(6):
    tmpi = data[i][0]
    tmpj = data[i][1]
    arr[tmpi][tmpj] = 1
    
print("有向圖")
for i in range(1,6):
    for j in range(1,6):
        print(f"[{arr[i][j]}]",end="")
    print()    
