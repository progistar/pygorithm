import sys
import math
from queue import PriorityQueue

N, M, R = map(int, sys.stdin.readline().split())
T = list(map(int, sys.stdin.readline().split()))
edges = list(list(map(int, sys.stdin.readline().split())) for _ in range(R))

graph = {}

for edge in edges:
    v1 = edge[0]
    v2 = edge[1]
    w  = edge[2]
    
    if graph.get(v1) == None:
        graph[v1] = []
        
    graph[v1].append([v2, w])
    
    if graph.get(v2) == None:
        graph[v2] = []
        
    graph[v2].append([v1, w])
    

max_get = 0
for s in range(1, N+1):
    dist = list(math.inf for _ in range(N+1))
    visit = list(False for _ in range(N+1))
    dist[s] = 0
    
    Q = PriorityQueue()
    Q.put((dist[s],s))
    
    while not Q.empty():
        d, v1 = Q.get()
        
        if visit[v1] or graph.get(v1) == None or d > M:
            continue
        
        visit[v1] = True
        
        for node in graph[v1]:
            v2 = node[0]
            w  = node[1]
            
            dist[v2] = min(dist[v2], dist[v1] + w)
            
            Q.put((dist[v2], v2))
            
    this_get = 0
    
    for i in range(1, N+1):
        if dist[i] != math.inf and dist[i] <= M:
            this_get = this_get + T[i-1]
            
    max_get = max(this_get, max_get)
    
print(max_get)