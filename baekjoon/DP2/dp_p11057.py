import sys
import math

D = 10007
N = (int) (sys.stdin.readline())
nums = [i for i in range(10)]

dp = [[0 for i in range(N)] for j in range(10)]

## PRE
for num in nums:
    dp[num][0] = 1

for n in range(1, N):
    for i in nums:
        for j in range(i, 10):
            dp[i][n] = (dp[i][n] + dp[j][n-1]) % D

S = 0
for i in range(10):
    S = (S + dp[i][N-1]) % D

print(S)