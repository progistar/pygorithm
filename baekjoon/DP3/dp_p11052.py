import sys
import math

N = (int) (sys.stdin.readline())
Ps = list(map(int, sys.stdin.readline().split()))

dp = list(0 for _ in range(N+1))

dp[1] = Ps[0]

for i in range(1,N+1):
    dp[i] = Ps[i-1]
    for j in range(1, i):
        dp[i] = max(dp[j]+dp[i-j], dp[i])

print(dp[N])