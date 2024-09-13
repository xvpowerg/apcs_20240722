def bfs(graph,start):
    visited = []
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            neigbors = graph[node]
            for n in neigbors:
                queue.append(n)
    return visited

graph = {'A':['B', 'C', 'D'],
         'B':['A', 'E'],
         'C':['A', 'F'],
         'D':['A', 'G', 'H'],
         'E':['B'],
         'F':['C', 'I', 'J'],
         'G':['D'],
         'H':['D'],
         'I':['F'],
         'J':['F']
        }

print(bfs(graph,"A"))
