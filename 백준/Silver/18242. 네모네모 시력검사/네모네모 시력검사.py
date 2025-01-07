import sys 
input = sys.stdin.readline 
from collections import deque 

n,m=map(int,input().split())
space=[]
for _ in range(n):
    space.append(list(map(str,input().strip())))

def in_range(r,c):
    return -1<r<n and -1<c<m

dr=[-1,0,1,0]
dc=[0,1,0,-1]

visit=[[False]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if space[i][j]=='#':
            queue=deque()
            queue.append((i,j))
            trace=deque()
            trace.append((i,j))
            visit[i][j]=True
            min_r,max_r=1e9,0
            min_c,max_c=1e9,0
            while queue:
                r,c=queue.popleft()
                min_r=min(min_r,r)
                max_r=max(max_r,r)
                min_c=min(min_c,c)
                max_c=max(max_c,c)
                for k in range(4):
                    nr=r+dr[k]
                    nc=c+dc[k]
                    if in_range(nr,nc) and not visit[nr][nc] and space[nr][nc]=='#':
                        visit[nr][nc]=True
                        queue.append((nr,nc))
                        trace.append((nr,nc))
            CHECK={'UP':(min_r,(min_c+max_c)//2),
                   'DOWN':(max_r,(min_c+max_c)//2),
                   'RIGHT':((min_r+max_r)//2,max_c),
                   'LEFT':((min_r+max_r)//2,min_c)}
            for key, (r,c) in CHECK.items():
                if (r,c) not in trace:
                    print(key)
                    exit()
