import sys
import math

N, M = map(int, sys.stdin.readline().split())

edges = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
dist = [math.inf for _ in range(N+1)]

dist[1] = 0

for _ in range(N-1):
    for edge in edges:
        v1 = edge[0]
        v2 = edge[1]
        w  = edge[2]
        
        dist[v2] = min(dist[v2], dist[v1]+w)
        
isNegCyclic = False
for edge in edges:
    v1 = edge[0]
    v2 = edge[1]
    w  = edge[2]
        
    if dist[v2] > (dist[v1]+w):
        isNegCyclic = True
        break

if isNegCyclic:
    print("-1")
else:
    for i in range(2, N+1):
        if dist[i] == math.inf:
            print("-1")
        else:
            print(dist[i])