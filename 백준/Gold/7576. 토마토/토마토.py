from collections import deque
import sys
input = sys.stdin.readline

#m=열, n=행
m,n = map(int,input().split())
space=[]
for _ in range(n):
    space.append(list(map(int,input().split())))

queue=deque()
for i in range(n):
    for j in range(m):
        if space[i][j]==1:
            queue.append((i,j))
dr=[1,0,-1,0]
dc=[0,-1,0,1]

while queue:
    r,c=queue.popleft()
    for i in range(4):
        nr=r+dr[i]
        nc=c+dc[i]
        if -1<nr<n and -1<nc<m and space[nr][nc]==0:
            space[nr][nc]=space[r][c]+1
            queue.append((nr,nc))
MAX=0
for row in space:
    for i in row:
        if i == 0:
            print(-1)
            exit()
    else:
        MAX=max(MAX,max(row))
print(MAX-1)

