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
    sum_start=0
    for i in start:
        for j in start:
            sum_start+=space[i][j]
    sum_link=0
    for i in link:
        for j in link:
            sum_link+=space[i][j]


    MIN=min(MIN,abs(sum_start-sum_link))
print(MIN)
    
    
