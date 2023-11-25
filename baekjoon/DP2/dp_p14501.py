import sys
import math

N = (int) (sys.stdin.readline())
TPs = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [0 for _ in range(N+1)]

for day in reversed(range(1, N+1)):
    T = TPs[day-1][0]
    P = TPs[day-1][1]
    
    if day + T > N +1:
        dp[day] = 0
    elif day + T == N+1:
        dp[day] = P
    else:
        dp[day] = P + dp[day+T]
        
    if day < N:
        dp[day] = max(dp[day], dp[day+1])

print(dp[1])