import sys
import math

N = (int) (sys.stdin.readline())

dp = list(list(0 for _ in range(10)) for __ in range(N))

for i in range(10):
    dp[0][i] = 1
    
for k in range(1, N):
    for i in range(0, 10):
        for j in range(i, 10):
            dp[k][j] = (dp[k][j] + dp[k-1][i]) % 10007


S = 0
for i in range(10):
    S = (S + dp[N-1][i]) % 10007
    
print(S)