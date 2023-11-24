import sys
import math

N = (int) (sys.stdin.readline())
S = list( (int) (sys.stdin.readline()) for _ in range(N))
D = 1000000009
M = 1000001
memorizer = list(0 for _ in range(M))

memorizer[1] = 1
memorizer[2] = 2
memorizer[3] = 4

for i in range(4,M):
    memorizer[i] = (memorizer[i-3] + memorizer[i-2] + memorizer[i-1]) % D
    
for s in S:
    print(memorizer[s])