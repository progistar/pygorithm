import sys
import math

N, K = map(int, sys.stdin.readline().split())
coins = list((int)(sys.stdin.readline()) for _ in range(N))

dp = [math.inf for _ in range(K+1)]

dp[0] = 0
for i in range(1,K+1):
    for coin in coins:
        if (i-coin) >= 0:
            dp[i] = min(dp[i], dp[i-coin]+1)

S = -1 if dp[K] == math.inf else dp[K]

print(S)