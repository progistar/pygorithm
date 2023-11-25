import sys
import math

N = (int) (sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

dp = [0 for _ in range(N)]


s_max = 0
for i in range(N):
    dp[i] = nums[i]
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = dp[j] + nums[i] if dp[i] < dp[j] + nums[i] else dp[i]
    s_max = max(s_max, dp[i])
print(s_max)