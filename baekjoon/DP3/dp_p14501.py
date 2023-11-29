import sys
import math

N = (int) (sys.stdin.readline())
TPs = list(list(map(int, sys.stdin.readline().split())) for _ in range (N))

income = list(0 for _ in range(N+1))
for i in reversed(range(1, N+1)):
    T = TPs[i-1][0]
    P = TPs[i-1][1]
    
    if (T+i-1) == N:
        income[i] = P
    elif (T+i-1) < N:
        income[i] = max(income[i+T] + P, income[i+1])
    
    if i < N:
        income[i] = max(income[i], income[i+1])

print(income[1])
    
import sys
import math
