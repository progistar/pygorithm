import sys
import math

N, M = map(int, sys.stdin.readline().split())

edges = list(list(map(int, sys.stdin.readline().split())) for _ in range(M))

in_degrees = list(0 for _ in range(N+1))

graph = {}
for edge in edges:
    v1 = edge[0]
    v2 = edge[1]
    
    if graph.get(v1) == None:
        graph[v1] = []
    graph[v1].append(v2)
    
    in_degrees[v2] = in_degrees[v2] + 1
    

zero_degrees = []
for i in range(1, N+1):
    if in_degrees[i] == 0:
        zero_degrees.append(i)

orders = []
while len(zero_degrees) != 0:
    v1 = zero_degrees.pop()
    orders.append(v1)
    
    if graph.get(v1) == None:
        continue
    
    for v2 in graph[v1]:
        in_degrees[v2] = in_degrees[v2] - 1
        
        if in_degrees[v2] == 0:
            zero_degrees.append(v2)
            

print(*orders)
    