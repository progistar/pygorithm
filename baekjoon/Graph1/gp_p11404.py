import sys
import math

num_cities = (int) (sys.stdin.readline())
num_lines  = (int) (sys.stdin.readline())

lines = list(list(map(int, sys.stdin.readline().split())) for _ in range(num_lines))

matrix = list(list(math.inf for _ in range(num_cities)) for __ in range(num_cities))

for line in lines:
    v1 = line[0]-1
    v2 = line[1]-1
    cost = line[2]
    
    matrix[v1][v2] = min(matrix[v1][v2], cost)

for k in range(num_cities):
    for i in range(num_cities):
        for j in range(num_cities):
            matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

for i in range(num_cities):
    for j in range(num_cities):
        if matrix[i][j] == math.inf:
            matrix[i][j] = 0
        if i == j:
            matrix[i][j] = 0
            
for row in matrix:
    print(*row)