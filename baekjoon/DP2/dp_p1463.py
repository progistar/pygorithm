import math
import sys

N = (int) (sys.stdin.readline())
dp = [math.inf for _ in range(N+1)]

dp[1] = 0
if N > 1:
    dp[2] = 1
if N > 2:
    dp[3] = 1

for i in range(4, N+1):
    
    # for 3
    v = (int) (i / 3)
    if v * 3 == i:
        dp[i] = min(dp[i], dp[v]+1)
    
    # for 2
    v = (int) (i / 2)
    if v * 2 == i:
        dp[i] = min(dp[i], dp[v]+1)
        
    # for -1
    v = i -1
    if v > 0:
        dp[i] = min(dp[i], dp[v]+1)

print(dp[N])