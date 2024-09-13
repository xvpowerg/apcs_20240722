def dfs(graph,node,path=[]):
        path += [node]
        for n in graph[node]:
            if n not in path:
                path = dfs(graph,n,path)
        return path
    
graph = {'V0':['V1', 'V2'],
         'V1':['V0', 'V3', 'V4'],
         'V2':['V0', 'V5', 'V6'],
         'V3':['V1', 'V7',],
         'V4':['V1', 'V7',],
         'V5':['V2', 'V7',],
         'V6':['V1', 'V7',],
         'V7':['V3', 'V4', 'V5', 'V6',]} 

print(dfs(graph,"V0"))
