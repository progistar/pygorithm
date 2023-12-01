import sys
import math
from queue import PriorityQueue

N, M = map(int, sys.stdin.readline().split())

dp = [math.inf for _ in range(200001)]
visit = [False for _ in range(200001)]

pq = PriorityQueue()

dp[N] = 0
pq.put([dp[N], N])

while not pq.empty():
    dist, v = pq.get()
    
    if visit[v]:
        continue
    visit[v] = True
    
    if v-1 >= 0:
        dp[v-1] = min(dp[v-1], dp[v]+1)
        pq.put([dp[v-1], v-1])
    if v+1 < 200001:
        dp[v+1] = min(dp[v+1], dp[v]+1)
        pq.put([dp[v+1], v+1])
    if 2*v < 200001:
        dp[2*v] = min(dp[2*v], dp[v])
        pq.put([dp[2*v], 2*v])

print(dp[M])