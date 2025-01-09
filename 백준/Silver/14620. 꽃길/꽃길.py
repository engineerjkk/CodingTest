import sys 
input = sys.stdin.readline 
from itertools import combinations

n=int(input())
space=[]
for _ in range(n):
    space.append(list(map(int,input().split())))

lst=[]
for i in range(1,n-1):
    for j in range(1,n-1):
        lst.append((i,j))

dr=[-1,0,1,0]
dc=[0,1,0,-1]

def in_range(r,c):
    return -1<r<n and -1<c<n

answer=1e9
for nCr in combinations(lst,3):
    visit=[[False]*n for _ in range(n)]
    for r,c in nCr:
        visit[r][c]=True 
        for i in range(4):
            nr=r+dr[i]
            nc=c+dc[i]
            if not visit[nr][nc]:
                visit[nr][nc]=True 
    cnt=0
    tmp=0
    for i in range(n):
        for j in range(n):
            if visit[i][j]:
                cnt+=1
                tmp+=space[i][j]
    if cnt==15:
        answer=min(answer,tmp)
print(answer)

