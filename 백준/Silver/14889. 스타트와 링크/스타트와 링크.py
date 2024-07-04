import sys
input = sys.stdin.readline
from itertools import combinations
n=int(input())
lst=[]
for _ in range(n):
    lst.append(list(map(int,input().split())))

tmp=[]
for i in range(n):
    tmp.append(i)
MIN=sys.maxsize
for nCr in combinations(tmp,n//2):
    start=list(nCr)
    link=[]
    for i in range(n):
        if i not in start:
            link.append(i)
    
    startSum=0
    linkSum=0
    
    for i in start:
        for j in start:
            startSum+=lst[i][j]
    for i in link:
        for j in link:
            linkSum+=lst[i][j]
    MIN=min(MIN,abs(startSum-linkSum))
print(MIN)

