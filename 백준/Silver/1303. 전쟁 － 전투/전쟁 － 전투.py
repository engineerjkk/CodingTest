import sys
input = sys.stdin.readline
from collections import deque

def in_range(r,c):
    return -1<r<n and -1<c<m

def solution(n,m,space):
    total_white=0
    total_blue=0
    visit=[[False]*m for _ in range(n)]
    dr=[-1,0,1,0]
    dc=[0,1,0,-1]
    
    for i in range(n):
        for j in range(m):
            if not visit[i][j]:
                queue=deque()
                queue.append((i,j))
                trace=deque()
                trace.append((i,j))
                visit[i][j]=True
                while queue:
                    r,c=queue.popleft()
                    for k in range(4):
                        nr=r+dr[k]
                        nc=c+dc[k]
                        if in_range(nr,nc) and space[nr][nc]==space[r][c] and not visit[nr][nc]:
                            queue.append((nr,nc))
                            trace.append((nr,nc))
                            visit[nr][nc]=True
                r,c=trace[0]
                if space[r][c]=='W':
                    total_white+=len(trace)*len(trace)
                else:
                    total_blue+=len(trace)*len(trace)
    return total_white,total_blue
                    


m,n=map(int,input().split())
space=[]
for _ in range(n):
    space.append(input().strip())
white,blue=solution(n,m,space)
print(white,blue)