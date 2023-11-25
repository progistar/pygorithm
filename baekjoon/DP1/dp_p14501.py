import sys
import math

N = (int) (sys.stdin.readline())
TP = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

S = list(0 for _ in range(N))
max_ = 0
for i in reversed(range(N)):
    T = TP[i][0]
    P = TP[i][1]
    
    if (i+T) == N:
        S[i] = P if max_ < P else max_
    elif (i+T) < N:
        S[i] = P + S[i+T] if max_ < P + S[i+T] else max_
    else:
        S[i] = max_
    
    max_ = S[i]
    
print(max_)