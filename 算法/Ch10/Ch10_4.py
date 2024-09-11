data=[[1,2],[2,1],[2,5],[5,2],                      #圖形陣列宣告
      [2,3],[3,2],[2,4],[4,2],
      [3,4],[4,3],[3,5],[5,3],
      [4,5],[5,4]]

graph = {}
for i in range(1,6):
    graph[i] = []
    
for j in range(len(data)):
    graph[data[j][0]].append(data[j][1])

for k in graph:
    print(f"頂點{k}=>",end="")
    for v in graph[k]:
        print(f"[{v}]",end="")
    print()
