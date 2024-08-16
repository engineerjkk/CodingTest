from collections import deque
def solution(maps):
    n=len(maps)
    m=len(maps[0])

    dr=[0,1,0,-1]
    dc=[-1,0,1,0]
    def in_range(r,c):
        return -1<r<n and -1<c<m
    def bfs(start,end,maps):
        space=[]
        for i in range(n):
            space.append(list(map(str,maps[i].strip())))
        flag=False
        queue=deque()
        visit=[[False]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if space[i][j]==start:
                    queue.append((i,j))
                    visit[i][j]=True
                    space[i][j]=0
                    flag=True
                    break
            if flag:
                break
        while queue:
            r,c=queue.popleft()
            for i in range(4):
                nr=r+dr[i]
                nc=c+dc[i]
                if in_range(nr,nc) and not visit[nr][nc] and space[nr][nc]!='X':
                    visit[nr][nc]=True
                    if space[nr][nc]==end:
                        space[nr][nc]=space[r][c]+1
                        return space[nr][nc]
                    space[nr][nc]=space[r][c]+1
                    queue.append((nr,nc))
        return -1
    
    path1=bfs('S','L',maps)
    path2=bfs('L','E',maps)
    if path1==-1 or path2==-1:
        return -1
    else:
        return path1+path2
