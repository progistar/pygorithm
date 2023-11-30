import sys
import math

N, M = map(int, sys.stdin.readline().split())

matrix = list(list(map(int, sys.stdin.readline().split())) for _ in range(N))
problems = list(list(map(int, sys.stdin.readline().split())) for _ in range(M))

dp = list(list(0 for _ in range(N)) for __ in range(N))

## init
dp[0][0] = matrix[0][0]
for i in range(1,N):
    dp[0][i] = matrix[0][i] + dp[0][i-1]
    dp[i][0] = matrix[i][0] + dp[i-1][0]
    
for i in range(1,N):
    for j in range(1,N):
        up = dp[i-1][j]
        left = dp[i][j-1]
        dig = dp[i-1][j-1]
        
        dp[i][j] = matrix[i][j] + up + left - dig
        
for problem in problems:
    row1 = problem[0] - 1
    col1 = problem[1] - 1
    
    row2 = problem[2] - 1
    col2 = problem[3] - 1
    
    dig = dp[row1-1][col1-1] if (row1 > 0) and (col1 > 0) else 0
    up = dp[row1-1][col2] if (row1 > 0) else 0
    left = dp[row2][col1-1] if (col1 > 0) else 0
    
    ans = dp[row2][col2] - up - left + dig
    print(ans)
    