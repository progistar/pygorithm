import sys
import math

N = (int) (sys.stdin.readline())

numbers = list(map(int, sys.stdin.readline().split()))
sum = [0 for _ in range (N)]

max = 0
for i in range(N):
    sum[i] = numbers[i]
    for j in range(i):
        if numbers[i] > numbers[j]:
            sum[i] = (sum[j] + numbers[i]) if sum[i] < (sum[j] + numbers[i]) else sum[i]
    max = (sum[i] if max < sum[i] else max)
    
print(max)