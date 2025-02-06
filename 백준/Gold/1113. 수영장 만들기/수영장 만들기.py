import sys 
input = sys.stdin.readline 
from collections import deque 
n,m=map(int,input().split())
space=[]
for _ in range(n):
    space.append(list(map(int,input().strip())))

dr=[-1,0,1,0]
dc=[0,1,0,-1]

def in_range(r,c):
    return -1<r<n and -1<c<m 

def bfs(i,j,height,visit):
    visit[i][j]=True
    count=1 
    flag=True
    queue=deque()
    queue.append((i,j))
    while queue:
        r,c=queue.popleft()
        for k in range(4):
            nr=r+dr[k]
            nc=c+dc[k]
            if not in_range(nr,nc):
                flag=False
                continue
            if space[nr][nc]<=height and not visit[nr][nc]:
                visit[nr][nc]=True 
                count+=1
                queue.append((nr,nc))
    if flag:
        return count
    else:
        return 0

answer=0
for height in range(1,9):
    visit=[[False]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if space[i][j]<=height and not visit[i][j]:
                answer+=bfs(i,j,height,visit)
print(answer)