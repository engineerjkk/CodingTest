import sys
input = sys.stdin.readline
from itertools import combinations

n,m=map(int,input().split())
space=[]
for _ in range(n):
    space.append(list(map(int,input().split())))

max_sum=0
for com in combinations(range(m),3):
    sum=0
    for i in range(n):
        tmp=0
        for j in com:
            tmp=max(tmp,space[i][j])
        sum+=tmp
    max_sum=max(max_sum,sum)
print(max_sum)