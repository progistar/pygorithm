import sys
import math
from queue import PriorityQueue

N = (int) (sys.stdin.readline())
M = (int) (sys.stdin.readline())

bus_lines = [(list(map(int, sys.stdin.readline().split()))) for _ in range(M)]
S, D = list(map(int, sys.stdin.readline().split()))
dists = [math.inf for _ in range(N+1)]
check = [False for _ in range(N+1)]

dict_edges = {}

for line in bus_lines:
    v1 = line[0]
    v2 = line[1]
    w  = line[2]
    
    if dict_edges.get(v1) == None:
        dict_edges[v1] = []
    dict_edges[v1].append([v2, w])

dists[S] = 0

pq = PriorityQueue()
pq.put((dists[S], S))

while not pq.empty():
    d1, v1 = pq.get()
    if check[v1]:
        continue
    check[v1] = True
    
    if dict_edges.get(v1) == None:
        continue
    
    for edge in dict_edges[v1]:
        v2 = edge[0]
        w  = edge[1]
        
        dists[v2] = min(dists[v2], d1 + w)
        pq.put((dists[v2], v2))

print(dists[D])