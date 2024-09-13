def bfs(node):
    global graph,queue,visited
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            if n not in visited:
                queue.append(n)
    if not queue:
        return
    else:
        nextNode = queue.pop(0)
        bfs(nextNode)

graph = {'V0':['V1', 'V2'],
         'V1':['V0', 'V3', 'V4'],
         'V2':['V0', 'V5', 'V6'],
         'V3':['V1', 'V7',],
         'V4':['V1', 'V7',],
         'V5':['V2', 'V7',],
         'V6':['V1', 'V7',],
         'V7':['V3', 'V4', 'V5', 'V6',]}
visited = []
queue = []
bfs("V0")
print(visited)
