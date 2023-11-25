import sys
import math

D = 1000000009

N = (int) (sys.stdin.readline())
M = list((int) (sys.stdin.readline()) for _ in range(N))
nums = [1,2,3]

S = [0 for _ in range(1000001)]

S[1] = 1
if N >= 2:
    S[2] = 2
if N >= 3:
    S[3] = 4

for i in range(4, len(S)):
    for num in nums:
        S[i] = (S[i-num] + S[i]) % D


for m in M:
    print(S[m])

