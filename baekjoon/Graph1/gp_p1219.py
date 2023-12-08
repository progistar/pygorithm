import math
import sys


N, S, D, M = map(int, sys.stdin.readline().split())

edges = list(list(map(int, sys.stdin.readline().split())) for _ in range(M))
earns = list(map(int, sys.stdin.readline().split()))

dist = list(-math.inf for _ in range(N))

dist[S] = earns[S]

for i in range(N-1):
    for edge in edges:
        v1 = edge[0]
        v2 = edge[1]
        w  = edge[2]
        
        dist[v2] = max(dist[v2], dist[v1] - w + earns[v2])

init_ans = dist[D]
## check the positive cycle
isInfinite  = False
for e in range(100):
    for edge in edges:
        v1 = edge[0]
        v2 = edge[1]
        w  = edge[2]

        if dist[v2] < (dist[v1] - w + earns[v2]):
            dist[v2] = math.inf

if init_ans < dist[D]:
    isInfinite = True

if dist[D] == -math.inf:
    print("gg")
elif isInfinite:
    print("Gee")
else:
    print(dist[D])
