from collections import deque
def solution(maps):
    answer = []
    space=[]
    for i in range(len(maps)):
        space.append(list(maps[i]))
    dr=[0,1,0,-1]
    dc=[-1,0,1,0]
    n=len(maps)
    m=len(maps[0])
    for i in range(n):
        for j in range(m):
            if space[i][j]=='X':
                space[i][j]=0
                continue
            space[i][j]=int(space[i][j])
    def in_range(r,c):
        return -1<r<n and -1<c<m
    def bfs(r,c):
        queue=deque()
        queue.append((r,c))
        visit=[[False]*m for _ in range(n)]
        visit[r][c]=True
        cnt=space[r][c]
        while queue:
            r,c=queue.popleft()
            for i in range(4):
                nr=r+dr[i]
                nc=c+dc[i]
                if in_range(nr,nc) and not visit[nr][nc] and space[nr][nc]!=0:
                    visit[nr][nc]=True
                    cnt+=space[nr][nc]
                    
                    space[nr][nc]=0
                    queue.append((nr,nc))
        return cnt
    
    for i in range(n):
        for j in range(m):
            if space[i][j]!=0:
                answer.append(bfs(i,j))
                print(".")
    if len(answer)>0:
        return sorted(answer)
    else:
        return [-1]
