import sys
import math

N,K = map(int, sys.stdin.readline().split())
coins = list((int) (sys.stdin.readline()) for _ in range(N))

dp = [0 for _ in range(K+1)]

dp[0] = 1
for coin in coins:
    for i in range(1, K+1):
        if i - coin >= 0:
            dp[i] = dp[i-coin] + dp[i]
            
print(dp[K])