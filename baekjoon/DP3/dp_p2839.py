import sys
import math

N = (int) (sys.stdin.readline())

dp = list(math.inf for _ in range(N+1))
sugars = [3,5]

dp[0] = 0

for i in range(3,N+1):
    for sugar in sugars:
        dp[i] = min(dp[i-sugar]+1, dp[i])
        
if dp[N] == math.inf:
    print("-1")
else:
    print(dp[N])