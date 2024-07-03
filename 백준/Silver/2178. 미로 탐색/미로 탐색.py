from collections import deque
import sys
input=sys.stdin.readline

#n=행, m=열
n,m = map(int,input().split())
space=[]
for _ in range(n):
    space.append(list(map(int,input().strip())))
visited=[[1]*m for _ in range(n)]

queue=deque()
queue.append((0,0))

dr=[1,0,-1,0]
dc=[0,-1,0,1]
while queue:
    r,c=queue.popleft()
    for i in range(4):
        nr=r+dr[i]
        nc=c+dc[i]
        if -1<nr<n and -1<nc<m and space[nr][nc]==1 and visited[nr][nc]==1:
            visited[nr][nc]=visited[r][c]+1
            queue.append((nr,nc))

print(visited[n-1][m-1])