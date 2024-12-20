import sys
input = sys.stdin.readline
from collections import deque

def solution(space,n,m):
    sharks=[]
    for i in range(n):
        for j in range(m):
            if space[i][j]==1:
                sharks.append((i,j))
    dr=[-1,-1,0,1,1,1,0,-1]
    dc=[0,1,1,1,0,-1,-1,-1]

    def in_range(r,c):
        return -1<r<n and -1<c<m
    
    def bfs():
        distance=[[-1]*m for _ in range(n)]
        queue=deque()
        for shark in sharks:
            r,c=shark
            distance[r][c]=0
            queue.append((r,c))
        while queue:
            r,c=queue.popleft()
            for i in range(8):
                nr=r+dr[i]
                nc=c+dc[i]
                if in_range(nr,nc) and distance[nr][nc]==-1:
                    distance[nr][nc]=distance[r][c]+1
                    queue.append((nr,nc))
        return distance

    distance=bfs()
    max_distance=0
    for i in range(n):
        for j in range(m):
            if space[i][j]==0:
                max_distance=max(max_distance,distance[i][j])
    return max_distance

n,m=map(int,input().split())
space=[]
for _ in range(n):
    space.append(list(map(int,input().split())))
print(solution(space,n,m))