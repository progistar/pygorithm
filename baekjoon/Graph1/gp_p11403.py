import sys
import math

N = (int) (sys.stdin.readline())

matrix = list(list(map(int, sys.stdin.readline().split())) for _ in range(N))

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 0:
            matrix[i][j] = math.inf


for k in range(N):
    for i in range(N):
        for j in range(N):
            matrix[i][j] = min(matrix[i][j], matrix[i][k]+matrix[k][j])

for i in range(N):
    for j in range(N):
        if matrix[i][j] == math.inf:
            matrix[i][j] = 0
        else:
            matrix[i][j] = 1

for row in matrix:
    print(*row)