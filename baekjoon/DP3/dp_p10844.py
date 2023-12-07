import sys
import math

N = (int) (sys.stdin.readline())

dp = list(list(0 for _ in range(10)) for __ in range(N))

dp[0][0] = 0
for i in range(1, 10):
    dp[0][i] = 1
    
for i in range(1, N):
    for j in range(0, 10):
        up, down = 0, 0
        
        if j > 0:
            up = dp[i-1][j-1]
            
        if j < 9:
            down = dp[i-1][j+1]
            
        dp[i][j] = (up + down)%1000000000


S = 0
for i in range(10):
    S = (S + dp[N-1][i]) % 1000000000
    
print(S)