import sys
input = sys.stdin.readline
from collections import deque
m,n=map(int,input().split())
space=[]
for _ in range(n):
    space.append(list(map(int,input().split())))

queue=deque()
for i in range(n):
    for j in range(m):
        if space[i][j]==1:
            queue.append((i,j))

dr=[-1,0,1,0]
dc=[0,1,0,-1]

def in_range(r,c):
    return -1<r<n and -1<c<m

visit=[[False]*m for _ in range(n)]

while queue:
    r,c=queue.popleft()
    visit[r][c]=True
    for i in range(4):
        nr=r+dr[i]
        nc=c+dc[i]
        if in_range(nr,nc) and not visit[nr][nc] and space[nr][nc]==0:
            space[nr][nc]=space[r][c]+1
            visit[nr][nc]=True
            queue.append((nr,nc))


for i in range(n):
    for j in range(m):
        if space[i][j]==0:
            print(-1)
            exit()

MAX=0
for i in range(n):
    for j in range(m):
        MAX=max(MAX,space[i][j])
print(MAX-1)
