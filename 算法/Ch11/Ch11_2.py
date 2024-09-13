def dfs(graph,start):
    path = []
    stack = [start]
    while stack:
        node = stack.pop()
        path.append(node)
        for n in graph[node]:
            stack.append(n)
    return path        
graph = {'A':['D', 'C', 'B'],
         'B':['E'],
         'C':['F'],
         'D':['H', 'G'],
         'E':[],
         'F':['J', 'I'],
         'G':[],
         'H':[],
         'I':[],
         'J':[]
        }
print(dfs(graph,"A"))
