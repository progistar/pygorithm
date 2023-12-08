import sys
import math
from queue import PriorityQueue

V, E = map(int, sys.stdin.readline().split())
S = (int) (sys.stdin.readline())

edges = list(list(map(int, sys.stdin.readline().split())) for _ in range(E))
graph = {}

for edge in edges:
    v1 = edge[0]
    v2 = edge[1]
    w  = edge[2]
    
    if graph.get(v1) == None:
        graph[v1] = []
    
    graph[v1].append([v2, w])


dist = list(math.inf for _ in range(V+1))
visit = list(False for _ in range(V+1))

dist[S] = 0

Q = PriorityQueue()
Q.put((dist[S], S))

while not Q.empty():
    d, v1 = Q.get()
    
    if visit[v1] or graph.get(v1) == None:
        continue
    visit[v1] = True
    
    for node in graph[v1]:
        v2 = node[0]
        w  = node[1]
        
        dist[v2] = min(dist[v2], dist[v1]+w)
        Q.put((dist[v2], v2))
        

for i in range(1, V+1):
    if dist[i] == math.inf:
        print("INF")
    else:
        print(dist[i])
    