from collections import deque
def solution(board):
    answer = 0
    flag=False
    n=len(board)
    m=len(board[0])
    queue=deque()
    visit=[[1e9]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j]=='R':
                queue.append((i,j,0))
                visit[i][j]=0
                flag=True
                break
        if flag:
            break
    dr=[0,1,0,-1]
    dc=[1,0,-1,0]
    
    def in_range(r,c):
        return -1<r<n and -1<c<m
    cnt=1
    while queue:
        r,c,dis=queue.popleft()
        if board[r][c]=='G':
            return dis
        for i in range(4):
            nr=r
            nc=c
            while in_range(nr+dr[i],nc+dc[i]) and board[nr+dr[i]][nc+dc[i]]!='D':
                nr+=dr[i]
                nc+=dc[i]
            if dis+1<visit[nr][nc]:
                visit[nr][nc]=dis+1
                queue.append((nr,nc,dis+1))


    
    return -1