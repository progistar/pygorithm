import sys
import math
from queue import PriorityQueue

V, E = map(int, sys.stdin.readline().split())
s = (int) (sys.stdin.readline())

edges = [list(map(int, sys.stdin.readline().split())) for _ in range(E)]

visit = [False for _ in range(V+1)]
dist  = [math.inf for _ in range(V+1)]

node_dict = {}

for edge in edges:
    v1 = edge[0]
    v2 = edge[1]
    w  = edge[2]
    
    if node_dict.get(v1) == None:
        node_dict[v1] = []
        
    node_dict[v1].append([v2, w])
    
pq = PriorityQueue()
dist[s] = 0

pq.put([dist[s], s])

while not pq.empty():
    d, v1 = pq.get()
    if visit[v1]:
        continue
    visit[v1] = True
    
    if node_dict.get(v1) == None:
        continue
    
    for v2, w in node_dict[v1]:
        dist[v2] = min(dist[v2], dist[v1] + w)
        pq.put([dist[v2], v2])

for i in range(1,V+1):
    if dist[i] == math.inf:
        print("INF")
    else:
        print(dist[i])
    