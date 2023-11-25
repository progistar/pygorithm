import sys
import math

N = (int) (sys.stdin.readline())
M = list(map(int, sys.stdin.readline().split()))

dp = [0 for _ in range(N+1)]

for i in range(1,N+1):
    dp[i] = M[i-1]
    for j in range(1, i):
        dp[i] = max(dp[i], dp[j] + dp[i-j])
        
print(dp[N])