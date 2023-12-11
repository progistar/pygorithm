import sys
import math

N, K = map(int, sys.stdin.readline().split())

coins = list((int) (sys.stdin.readline()) for _ in range(N))
dp = list(math.inf for _ in range(K+1))

for i in range(N):
    if coins[i] <= K:
        dp[coins[i]] = 1

for i in range(1,K+1):
    for j in range(N):
        coin = coins[j]
        
        if coin < i:
            dp[i] = min(dp[i], dp[i-coin]+1)
            
if dp[K] == math.inf:
    print("-1")
else:
    print(dp[K])