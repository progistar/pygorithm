import sys
import math

N, M = map(int, sys.stdin.readline().split())
bus_lines = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

dist = [math.inf for _ in range(N+1)]
dist[1] = 0

for i in range(N-1):
    for edge in bus_lines:
        v1 = edge[0]
        v2 = edge[1]
        w  = edge[2]
        dist[v2] = min(dist[v2], dist[v1]+w)
        
## negative cycle check
isNegativeCyclic = False
for edge in bus_lines:
    v1 = edge[0]
    v2 = edge[1]
    w  = edge[2]
    if dist[v2] != min(dist[v2], dist[v1]+w):
        isNegativeCyclic = True
        break


    
if isNegativeCyclic:
    print(-1)
else:
    for i in range(2,N+1):
        if dist[i] == math.inf:
            print(-1)
        else:
            print(dist[i])