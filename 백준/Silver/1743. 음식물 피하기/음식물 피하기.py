import sys
input = sys.stdin.readline
from collections import deque
n,m,k=map(int,input().split())
lst=[]
for _ in range(k):
    a,b=map(int,input().split())
    lst.append([a-1,b-1])

space=[[0]*m for _ in range(n)]
for i,j in lst:
    space[i][j]=1



dr=[-1,0,1,0]
dc=[0,1,0,-1]

def in_range(r,c):
    return -1<r<n and -1<c<m

def bfs(r,c,space):
    queue=deque()
    queue.append((r,c))
    space[r][c]=0
    cnt=1
    while queue:
        r,c=queue.popleft()
        for i in range(4):
            nr=r+dr[i]
            nc=c+dc[i]
            if in_range(nr,nc) and space[nr][nc]==1:
                queue.append((nr,nc))
                space[nr][nc]=0
                cnt+=1

    return cnt
answer=[0]
MAX=0
for r in range(n):
    for c in range(m):
        if space[r][c]==1:
            MAX=max(MAX,bfs(r,c,space))
print(MAX)





