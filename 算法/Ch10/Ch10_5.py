data=[[1,2],[2,1],[2,3],[2,4],[4,3],[4,1]]          #圖形陣列宣告

graph = dict()
for i in range(1,6):
    graph[i] = []

for j in range(len(data)):
    graph[data[j][0]].append(data[j][1])
    
for k in graph:
    print(f"頂點:{k}",end="")
    for x  in graph[k]:
        print(f"[{x}]",end="")
    print()    
    
