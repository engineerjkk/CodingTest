import sys
input = sys.stdin.readline
from itertools import combinations
n=int(input())
space=[]
for _ in range(n):
    space.append(list(map(int,input().split())))
lst=[]
for i in range(n):
    lst.append(i)
MIN=sys.maxsize
for start in combinations(lst,n//2):
    link=[]
    for i in lst:
        if i not in start:
            link.append(i)
    start_sum=0
    for i in start:
        for j in start:
            start_sum+=space[i][j]
    link_sum=0
    for i in link:
        for j in link:
            link_sum+=space[i][j]
    MIN=min(MIN,abs(start_sum-link_sum))
print(MIN)