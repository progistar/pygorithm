import sys
import math

N, M = map(int, sys.stdin.readline().split())

## N by N matrix
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

## a number of problems
problems = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

## pre-built acc. matrix
prebuilt_matrix = [list(0 for _ in range(N)) for __ in range(N)]

# initialize the pre-built matrix
prebuilt_matrix[0][0] = matrix[0][0]
for j in range(1, N):
    prebuilt_matrix[0][j] = prebuilt_matrix[0][j-1] + matrix[0][j]
for i in range(1, N):
    prebuilt_matrix[i][0] = prebuilt_matrix[i-1][0] + matrix[i][0]

# build the pre-built matrix by accumulating cells
for i in range(1, N):
    for j in range(1, N):
        prebuilt_matrix[i][j] = matrix[i][j] + prebuilt_matrix[i-1][j] + prebuilt_matrix[i][j-1] - prebuilt_matrix[i-1][j-1]
    
## solution
for p in problems:
    x1, y1 = p[0], p[1]
    x2, y2 = p[2], p[3]
    
    full = prebuilt_matrix[x2-1][y2-1]
    up_side = prebuilt_matrix[x2-1][y1-2] if y1 > 1 else 0
    left_side = prebuilt_matrix[x1-2][y2-1] if x1 > 1 else 0
    overlap_side = prebuilt_matrix[x1-2][y1-2] if (x1 > 1 and y1 > 1) else 0
    
    full = full - (up_side + left_side - overlap_side)
    print(full)
