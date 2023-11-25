import sys
import math

N = (int) (sys.stdin.readline())

dp = [math.inf for _ in range(N+1)]
sugars = [3, 5]

for sugar in sugars:
    if sugar <= N:
        dp[sugar] = 1

for i in range(1,N+1):
    for sugar in sugars:
        if (i-sugar) >= 0:
            dp[i] = min(dp[(i-sugar)] + 1, dp[i])

S = -1 if dp[N] == math.inf else dp[N]
print(S)