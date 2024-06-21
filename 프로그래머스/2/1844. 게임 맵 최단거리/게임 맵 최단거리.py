from collections import deque

def solution(maps):
    
    def in_range(r,c):
        return -1<r<n and -1<c<m
    
    answer = 0
    dr=[0,0,1,-1]
    dc=[1,-1,0,0]
    n=len(maps)
    m=len(maps[0])
    if n+m<4:
        return 2
    back=[[0]*(m) for _ in range(n)]
    visit=[[False]*(m) for _ in range(n)]
    queue=deque()
    queue.append((0,0))
    visit[0][0]=True
    can_reach=False
    while queue:
        r,c=queue.popleft()
        if r==n-1 and c==m-1:
            can_reach=True
            break
        for i in range(4):
            nr=r+dr[i]
            nc=c+dc[i]
            if in_range(nr,nc) and not visit[nr][nc] and maps[nr][nc]==1:
                visit[nr][nc]=True
                back[nr][nc]=(r,c)
                queue.append((nr,nc))
    if not can_reach:
        return -1
    else:
        cr,cc=back[n-1][m-1]
        answer=2
        while True:
            cr,cc=back[cr][cc]
            answer+=1
            #print(cr,cc)
            if cr==0 and cc==0:
                return answer
        
#maps=[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
#print(solution(maps))