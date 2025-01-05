import sys 
input = sys.stdin.readline 
from collections import deque

n,m=map(int,input().split())
space=[]
for _ in range(n):
    space.append(list(map(str,input().strip())))

dr=[-1,0,1,0]
dc=[0,1,0,-1]

def in_range(r,c):
    return -1<r<n and -1<c<m


visit=[[False]*m for _ in range(n)]
yang=0
wolf=0
for i in range(n):
    for j in range(m):
        if not visit[i][j] and (space[i][j]=='v' or space[i][j]=='o'):
            queue=deque()
            queue.append((i,j))
            visit[i][j]=True
            wolf_num=0
            yang_num=0
            if space[i][j]=='v':
                wolf_num+=1
            else:
                yang_num+=1
            while queue:
                r,c=queue.popleft()
                for k in range(4):
                    nr=r+dr[k]
                    nc=c+dc[k]
                    if in_range(nr,nc) and not visit[nr][nc] and space[nr][nc]!='#':
                        visit[nr][nc]=True 
                        queue.append((nr,nc))
                        if space[nr][nc]=='v':
                            wolf_num+=1
                        elif space[nr][nc]=='o':
                            yang_num+=1
            if yang_num>wolf_num:
                yang+=yang_num
            else:
                wolf+=wolf_num
print(yang,wolf)

