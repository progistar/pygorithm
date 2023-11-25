# increasing numbers
import sys
import math

N = (int) (sys.stdin.readline())
D = 10007
numbers = list(i for i in range(10))

memorizer = list(list(0 for _ in range(N)) for __ in numbers)

# init
for i in numbers:
    memorizer[i][0] = 1

for i in range(1, N):
    for n in numbers:
        for k in range(n, 10):
            memorizer[n][i] = (memorizer[n][i] + memorizer[k][i-1]) % D
            

sum = 0
for i in numbers:
    sum = (sum + memorizer[i][N-1]) % D
    
print(sum)