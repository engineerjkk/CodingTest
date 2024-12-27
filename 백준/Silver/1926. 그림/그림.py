from collections import deque
import sys
input = sys.stdin.readline

#n=행, m=열
n,m = map(int,input().split())

space=[]
for _ in range(n):
    space.append(list(map(int,input().split())))

dr=[1,0,-1,0]
dc=[0,-1,0,1]

def bfs(space,r,c):
    queue=deque()
    queue.append((r,c))
    space[r][c]=0
    count=1
    while queue:
        r,c=queue.popleft()
        for num in range(4):
            nr=r+dr[num]
            nc=c+dc[num]
            if -1<nr<n and -1<nc<m and space[nr][nc]==1:
                space[nr][nc]=0
                queue.append((nr,nc))
                count+=1
    return count



total=[]
num_picture=0
for i in range(n):
    for j in range(m):
        if space[i][j]==1:
            num_picture+=1
            cnt=bfs(space,i,j)
            total.append(cnt)
print(num_picture)
if len(total)==0:
    print(0)
else:
    print(max(total))
