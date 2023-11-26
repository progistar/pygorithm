import sys
import math

N, M, R = map(int, sys.stdin.readline().split())

edges =[list(map(int, sys.stdin.readline().split())) for _ in range(M)]
order = [0 for _ in range(N)]
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

stack = [R]
isVisited = {}
while len(stack) != 0:
    v = stack.pop()
    
    if isVisited.get(v) == None:
        isVisited[v] = True    
        order[v-1] = len(isVisited)
        if graph.get(v) != None:
            for edge in graph[v]:
                stack.append(edge)

for i in order:
    print(i)
    
