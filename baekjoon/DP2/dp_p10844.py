import sys
import math

D = 1000000000
N = (int) (sys.stdin.readline())

dp = [[0 for _ in range(N)] for __ in range(10)]

for i in range(10):
    dp[i][0] = 1

for i in range(1,N):
    dp[0][i] = dp[1][i-1]
    dp[9][i] = dp[8][i-1]
    for j in range(1, 9):
        dp[j][i] = (dp[j-1][i-1] + dp[j+1][i-1])%D

S = 0
for i in range(1,10):
    S = (S + dp[i][N-1])%D

print(S)