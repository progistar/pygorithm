import sys
import math

N = (int) (sys.stdin.readline())
nums = list((int) (sys.stdin.readline()) for _ in range(N))

def linear_sort(r1, r2):
    n3 = [0] * (len(r1) + len(r2))
    i = 0
    j = 0
    idx = 0
    while(idx < len(n3)):

        if i == len(r1):
            n3[idx] = r2[j]
            j = j+1
        elif j == len(r2):
            n3[idx] = r1[i]
            i = i+1
        elif r1[i] < r2[j]:
            n3[idx] = r1[i]
            i = i+1
        else:
            n3[idx] = r2[j]
            j = j+1
        
        idx = idx+1

    return n3

def swap (n):
    if n[0] > n[1]:
        tmp = n[0]
        n[0] = n[1]
        n[1] = tmp
    
    return n

def merge (n1, n2):
    if len(n1) == 1 or len(n2) == 1:
        if len(n1) == 2:
            n1 = swap(n1)
        elif len(n2) == 2:
            n2 = swap(n2)

        return linear_sort(n1, n2)

    m = (int) (len(n1)/2)
    r1 = merge (n1[0:m], n1[m:len(n1)])
    m = (int) (len(n2)/2)
    r2 = merge (n2[0:m], n2[m:len(n2)])

    return linear_sort(r1, r2)


ans = merge(nums[0:(int) (N/2)], nums[(int)(N/2):N])
for i in ans:
    print(i)