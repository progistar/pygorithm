import sys
import math
from queue import PriorityQueue

def dijkstra(v1, v2, N, graph):

    visit = [False for _ in range(N+1)]
    dist = [math.inf for _ in range(N+1)]
    
    pq = PriorityQueue()
    dist[v1] = 0
    pq.put([0, v1])
    
    while not pq.empty():
        _, v = pq.get()
        
        if visit[v]:
            if v == v2:
                return dist[v2]
            continue
        visit[v] = True
        
        if graph.get(v) == None:
            continue
        
        for edge in graph[v]:
            v_, d = edge[0], edge[1]
            dist[v_] = min(dist[v_], dist[v] + d)
            pq.put([dist[v_], v_])
        
    
    return dist[v2]


N, E = map(int, sys.stdin.readline().split())

edges = list(list(map(int, sys.stdin.readline().split())) for _ in range(E))
v1, v2 = map(int, sys.stdin.readline().split())



graph = {}

for edge in edges:
    source, dest, dist = edge[0], edge[1], edge[2]
    
    if graph.get(source) == None:
        graph[source] = []
    graph[source].append([dest, dist])
    
    if graph.get(dest) == None:
        graph[dest] = []
    graph[dest].append([source, dist])


source_to_v1 = dijkstra(1, v1, N, graph)
source_to_v2 = dijkstra(1, v2, N, graph)
v1_to_dest = dijkstra(v1, N, N, graph)
v2_to_dest = dijkstra(v2, N, N, graph)
mid_point = dijkstra(v1, v2, N, graph)

opt_path = min(source_to_v1+mid_point+v2_to_dest, source_to_v2+mid_point+v1_to_dest)

if opt_path == math.inf:
    print("-1")
else:
    print(opt_path)