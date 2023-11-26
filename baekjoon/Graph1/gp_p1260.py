import sys
import math

N, M, R = map(int, sys.stdin.readline().split())

edges =[list(map(int, sys.stdin.readline().split())) for _ in range(M)]
order = []
graph = {}
for edge in edges:
    v1 = edge[0]
    v2 = edge[1]
    if graph.get(v1) == None:
        graph[v1] = [v2]
    else:
        graph[v1].append(v2)
        
    if graph.get(v2) == None:
        graph[v2] = [v1]
    else:
        graph[v2].append(v1)
        
for v1, Vs in graph.items():
    Vs.sort(reverse = True)

## DFS
stack = [R]
isVisited = {}
while len(stack) != 0:
    v = stack.pop()
    
    if isVisited.get(v) == None:
        isVisited[v] = True    
        order.append(v)
        if graph.get(v) != None:
            for edge in graph[v]:
                stack.append(edge)

## BFS
print(*order, sep =' ')

for v1, Vs in graph.items():
    Vs.sort(reverse = False)
    
queue = [R]
order = []
isVisited = {}
while len(queue) != 0:
    v = queue.pop(0)
    
    if isVisited.get(v) == None:
        isVisited[v] = True    
        order.append(v)
        if graph.get(v) != None:
            for edge in graph[v]:
                queue.append(edge)
print(*order, sep =' ')