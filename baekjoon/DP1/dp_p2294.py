import sys
import math


N, K = map(int, sys.stdin.readline().split())

coins = list( (int) (sys.stdin.readline()) for _ in range(N))

memorizer = list(math.inf for _ in range(K+1))

memorizer[0] = 0
for i in range(1,K+1):
    for c in coins:
        if (i - c) >= 0:
            memorizer[i] = memorizer[(i-c)] + 1 if memorizer[i] > (memorizer[(i-c)]+1) else memorizer[i]

if memorizer[K] == math.inf:
    memorizer[K] = -1
    
print(memorizer[K])