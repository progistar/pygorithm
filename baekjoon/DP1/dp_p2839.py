import sys
import math

values = [math.inf for n in range(0,5001)]
sugar_set = [3, 5]


## take an input
N = (int) (sys.stdin.readline())

values[0] = 0
for n in range(3, N+1):
    for s in sugar_set:
        if (n - s) >= 0:
            values[n] = (values[n-s]+1) if values[n] > (values[n-s]+1) else values[n]
    
## Set -1 value for invalid input
for n in range(3, N+1):
    values[n] = -1 if values[n] == math.inf else values[n]

print(values[N])