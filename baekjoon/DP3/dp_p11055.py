import sys
import math

N = (int) (sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
dp = list(0 for _ in range(N))

for i in range(N):
    dp[i] = nums[i]
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j]+nums[i])


max_ = 0
for i in range(N):
    max_ = max(dp[i], max_)
    
print(max_)