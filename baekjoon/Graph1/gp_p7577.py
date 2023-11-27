import sys
import math

import sys
import math

K, N = map(int, sys.stdin.readline().split())
input = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dist = [math.inf for _ in range(K+2)]
src = K+1
edges = []


for i in range(0, K):
    edges.append([i, i+1, 1])
    edges.append([i+1, i, 0])

for i in input:
    edges.append([i[1], i[0]-1, -i[2]])
    edges.append([i[0]-1, i[1], i[2]])

for i in range(0, K+1):
    edges.append([src, i, 0])

dist[src] = 0
for i in range(K+1):
    for edge in edges:
        v1 = edge[0]
        v2 = edge[1]
        w = edge[2]
        dist[v2] = min(dist[v1]+w, dist[v2])

isNegCyclic = False
for edge in edges:
    v1 = edge[0]
    v2 = edge[1]
    w = edge[2]
    if dist[v2] != min(dist[v1]+w, dist[v2]):
        isNegCyclic = True
        break

if isNegCyclic:
    print("NONE")
else:
    output = []
    for i in range(1,K+1):
        if dist[i-1] == dist[i]:
            output.append("-")
        else:
            output.append("#")
    S = ''.join(x for x in output)
    print(S)