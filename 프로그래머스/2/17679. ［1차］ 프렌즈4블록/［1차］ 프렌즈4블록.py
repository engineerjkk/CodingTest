def check(n,m,board):
    tmp=[[0]*m for _ in range(n)]
    for r in range(n-1):
        for c in range(m-1):
            if board[r][c]==board[r][c+1]==board[r+1][c]==board[r+1][c+1] and board[r][c]!="0":
                tmp[r][c]=1
                tmp[r][c+1]=1
                tmp[r+1][c]=1
                tmp[r+1][c+1]=1
    cnt=0
    for r in range(n):
        for c in range(m):
            if tmp[r][c]==1:
                cnt+=1
                board[r][c]="0"
    
    if cnt==0:
        return 0
    
    for r in range(n-2,-1,-1):
        for c in range(m):
            t=r
            while -1<t+1<n and board[t+1][c]=="0":
                t+=1
            if t!=r:
                board[t][c]=board[r][c]
                board[r][c]="0"
    return cnt

def solution(n, m, board):
    answer = 0
    board=list(map(list,board))
    while True:
        cnt=check(n,m,board)
        if cnt==0:
            break
        answer+=cnt
    return answer