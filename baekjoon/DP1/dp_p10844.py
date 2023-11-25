import sys
import math

## DFS + Memorization

N = (int) (sys.stdin.readline())
D = 1000000000

values = [n for n in range(10)]

matrix = [list(0 for _ in range(10)) for __ in range(N)]

for i in values:
    matrix[N-1][i] = 1

for i in reversed(range(N-1)):
    for v1 in values:
        for v2 in values:
            if abs(v1-v2) == 1:
                matrix[i][v1] = (matrix[i][v1] + matrix[i+1][v2]) % D

sum = 0

for i in range(1,10):
    sum = (sum + matrix[0][i]) % D
    
print(sum)