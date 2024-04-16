from collections import deque
import sys
input = sys.stdin.readline

#t=높이, m=열, n=행
m,n,t=map(int,input().split())

space=[]
for _ in range(t):
    temp=[]
    for _ in range(n):
        temp.append(list(map(int,input().split())))
    space.append(temp)

queue=deque()
for i in range(t):
    for j in range(n):
        for k in range(m):
            if space[i][j][k]==1:
                queue.append((i,j,k))

dh=[1,-1,0,0,0,0]
dr=[0,0,1,-1,0,0]
dc=[0,0,0,0,1,-1]

while queue:
    h,r,c=queue.popleft()
    for i in range(6):
        nh=h+dh[i]
        nr=r+dr[i]
        nc=c+dc[i]
        if -1<nh<t and -1<nr<n and -1<nc<m and space[nh][nr][nc]==0:
            space[nh][nr][nc]=space[h][r][c]+1
            queue.append((nh,nr,nc))
MAX=0
real_MAX=0
for rec in space:
    for row in rec:
        for i in row:
            if i == 0:
                print(-1)
                exit()
        else:
            MAX=max(MAX,max(row))
    real_MAX=max(real_MAX,MAX)
print(real_MAX-1)
