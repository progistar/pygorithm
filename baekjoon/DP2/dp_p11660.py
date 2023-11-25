import sys
import math

N, M = map(int, sys.stdin.readline().split())

matrix = [list(map(int, sys.stdin.readline().split())) for _ in range (N)]
coordinates = [list(map(int, sys.stdin.readline().split())) for _ in range (M)]

sum_table = [list(0 for _ in range (N)) for __ in range(N)]

## PRE: calculate dynamic programming
sum_table[0][0] = matrix[0][0]
for i in range(1, N):
    sum_table[0][i] = matrix[0][i] + sum_table[0][i-1]
for i in range(1, N):
    sum_table[i][0] = matrix[i][0] + sum_table[i-1][0]

for i in range(1, N):
    for j in range(1, N):
        sum_table[i][j] = matrix[i][j] + (sum_table[i-1][j] + sum_table[i][j-1] - sum_table[i-1][j-1])
        
## Get the solutions
for row_col in coordinates:
    row1, col1 = row_col[0]-1, row_col[1]-1
    row2, col2 = row_col[2]-1, row_col[3]-1
    
    all = sum_table[row2][col2]
    sub_up = sum_table[row1-1][col2] if row1-1 >= 0 else 0
    sub_left = sum_table[row2][col1-1] if col1-1 >= 0 else 0
    sub = sum_table[row1-1][col1-1] if (row1-1 >= 0) and (col1-1 >= 0) else 0
    
    all = all - (sub_up + sub_left - sub)
    
    print(all)
    