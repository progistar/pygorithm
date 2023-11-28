import sys
import math

N, M, R = map(int, sys.stdin.readline().split())

edges = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
check = [0 for _ in range(N+1)]

graph = {}

for edge in edges:
    v1 = edge[0]
    v2 = edge[1]
    
    if graph.get(v1) == None:
        graph[v1] = []
    graph[v1].append(v2)
    
    if graph.get(v2) == None:
        graph[v2] = []
    graph[v2].append(v1)

for idx in graph.keys():
    graph[idx].sort(reverse = True)

stack = []

stack.append(R)
order = 1
while len(stack) != 0:
    v1 = stack.pop()
    if check[v1] != 0:
        continue
    
    check[v1] = order
    order = order + 1
    if graph.get(v1) != None:
        for v in graph[v1]:
            stack.append(v)

for idx in range(1, N+1):
    print(check[idx])    