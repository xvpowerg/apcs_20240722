data=[[1,2],[2,1],[2,3],[2,4],[4,3],[4,1]]          #圖形陣列宣告

graph = {i:[] for i in range(1,6)}

for v in data:
    graph[v[0]].append(v[1])
    
for k in graph:
    print(f"頂點:{k}",end="")
    for x  in graph[k]:
        print(f"[{x}]",end="")
    print()    
