import sys
import math

# coin 1

import sys
import math

N, K = map(int, sys.stdin.readline().split())
coins = list((int) (sys.stdin.readline()) for _ in range(N))

matrix = list(0 for _ in range(K+1))

## initialize the first coin
for k in range(K+1):
    if k % coins[0] == 0:
        matrix[k] = 1

for cidx in range(1, len(coins)):
    cur_coin = coins[cidx]
    prv_coin = coins[cidx-1]
    for k in range(K+1):
        if k - cur_coin >= 0:
            matrix[k] = matrix[k] + matrix[k-cur_coin]

print(matrix[K])
