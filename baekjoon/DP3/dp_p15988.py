import sys
import math

D = 1000000009
N = (int) (sys.stdin.readline())
C = list((int) (sys.stdin.readline()) for _ in range(N))

nums = [1,2,3]
dp = [0 for _ in range(1000001)]

dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, len(dp)):
    ## for loop을 도는 것 보다는 hard coding해서 나열하는 것이 % 연산이 적어져서 더 빠름.
    # 두배 정도 더 빨라짐 (ex> for loop took ~932 ms V.S. hard coding took ~488-524 ms)
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3] + dp[i]) % D
        
for c in C:
    print(dp[c])
