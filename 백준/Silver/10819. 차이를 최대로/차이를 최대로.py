import sys
from collections import deque
from itertools import permutations
input = sys.stdin.readline

n=int(input())
lst=list(map(int,input().split()))

nCr=permutations(lst,n)
answer=0
for x in nCr:
    total=0
    for i in range(len(x)-1):
        total+=abs(x[i]-x[i+1])
    answer=max(answer,total)
print(answer)

