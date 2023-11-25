import sys
import math

N = (int) (sys.stdin.readline())

M = math.inf

memorizer = [math.inf for _ in range(N+1)]

memorizer[1] = 0

if N > 1:
    memorizer[2] = 1

if N > 2:
    memorizer[3] = 1

for i in range(4,N+1):
    j = (int) (i / 2)
    
    if (j * 2 == i) and memorizer[j] != math.inf:
        memorizer[i] = (memorizer[j]+1) if memorizer[i] > (memorizer[j]+1) else memorizer[i]

    j = (int) (i / 3)
    if (j * 3 == i) and memorizer[j] != math.inf:
        memorizer[i] = (memorizer[j]+1) if memorizer[i] > (memorizer[j]+1) else memorizer[i]
    
    j = i -1
    if memorizer[j] != math.inf:
        memorizer[i] = (memorizer[j]+1) if memorizer[i] > (memorizer[j]+1) else memorizer[i]

print(memorizer[N])