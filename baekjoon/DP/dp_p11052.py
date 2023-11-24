import sys
import math

N = (int) (sys.stdin.readline())
P = list(map(int, sys.stdin.readline().split()))

card_nums = list((i+1) for i in range(len(P)))
memorizer = list(0 for _ in range(N+1))
for i in range(1, N+1):
    for n in card_nums:
        if i-n >= 0:
            pay = memorizer[i-n] + P[n-1]
            memorizer[i] = pay if memorizer[i] < pay else memorizer[i]

print(memorizer[N])