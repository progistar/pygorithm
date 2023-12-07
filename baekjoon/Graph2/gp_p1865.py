import sys
import math

TC = (int) (sys.stdin.readline())
INF = 10000 * 2501
ans = []
for i in range(TC):
    
    NMW = list(map(int, sys.stdin.readline().split()))
    N = NMW[0]
    M = NMW[1]
    W = NMW[2]
    loads = list(list(map(int, sys.stdin.readline().split())) for _ in range(M))
    wamrs = list(list(map(int, sys.stdin.readline().split())) for _ in range(W))
    
    edges = []

    for load in loads:
        v1 = load[0]
        v2 = load[1]
        w = load[2]
        
        edges.append([v1, v2, w])
        edges.append([v2, v1, w])
        

    for warm in wamrs:
        v1 = warm[0]
        v2 = warm[1]
        w = -warm[2]
        
        edges.append([v1, v2, w])

    dp = list(INF for _ in range(N+1))
    dp[1] = 0
    for i in range(N-1):
        for edge in edges:
            v1 = edge[0]
            v2 = edge[1]
            w  = edge[2]
            dp[v2] = min(dp[v2], dp[v1] + w)
    
    isNegCycle = False
    for edge in edges:
        v1 = edge[0]
        v2 = edge[1]
        w  = edge[2]
        if dp[v2] != min(dp[v2], dp[v1] + w):
            isNegCycle = True
            break
    
    if isNegCycle:
        ans.append("YES")
    else:
        ans.append("NO")

for a in ans:
    print(a)
            


