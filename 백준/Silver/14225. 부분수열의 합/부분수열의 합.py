import sys
input = sys.stdin.readline
from itertools import combinations

n=int(input())
lst=list(map(int,input().split()))
MAX=100000*20
visit=[False]*(MAX+1)

for i in range(1,n+1):
    for nCr in combinations(lst,i):
        a=sum(nCr)
        if a>MAX+1:
            continue
        visit[a]=True

answer=0
for i in range(1,MAX+1):
    if visit[i]==False:
        print(i)
        exit()