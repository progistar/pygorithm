import sys
import math

T = (int) (sys.stdin.readline())

dist = [math.inf for __ in range(501)]
ans = []
for _ in range(T):
    N, M, W = map(int, sys.stdin.readline().split())
    
    # undirected edges
    m_edges = [list(map(int, sys.stdin.readline().split())) for __ in range(M)]
    # directed edges with minus weight
    w_edges = [list(map(int, sys.stdin.readline().split())) for __ in range(W)]
    
    edges = []
    
    for edge in m_edges:
        v1 = edge[0]
        v2 = edge[1]
        w = edge[2]
        edges.append([v1, v2, w])
        edges.append([v2, v1, w])
    
    for edge in w_edges:
        v1 = edge[0]
        v2 = edge[1]
        w = edge[2]
        edges.append([v1, v2, -w])
        
    # do Bellman-ford
    isNegCyclic = False
    
    for s in range(1, 2):
        if isNegCyclic:
            break
        
        for i in range(N+1):
            dist[i] = 2000000000
        
        dist[s] = 0
        for __ in range(N-1):
            for edge in edges:
                v1 = edge[0]
                v2 = edge[1]
                w = edge[2]
                dist[v2] = min(dist[v2], dist[v1] + w)
                
        ## check negative cycle
        for edge in edges:
            v1 = edge[0]
            v2 = edge[1]
            w = edge[2]
            if dist[v2] != min(dist[v2], dist[v1] + w):
                isNegCyclic = True
                break
        
    if isNegCyclic:
        ans.append("YES")
    else:
        ans.append("NO")

for an in ans:
    print(an)