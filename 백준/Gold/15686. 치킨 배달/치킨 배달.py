import sys
input = sys.stdin.readline
from itertools import combinations

n,m=map(int,input().split())
space=[]
for _ in range(n):
    space.append(list(map(int,input().split())))

home=[]
chicken=[]
for i in range(n):
    for j in range(n):
        if space[i][j]==2:
            chicken.append((i,j))
        if space[i][j]==1:
            home.append((i,j))

answer=1e9
for nCr in combinations(chicken,m):
    result=0
    for r,c in home:
        MIN=1e9
        for nr,nc in nCr:
            tmp=abs(r-nr)+abs(c-nc)
            MIN=min(MIN,tmp)
        result+=MIN
    answer=min(result,answer)
print(answer)

