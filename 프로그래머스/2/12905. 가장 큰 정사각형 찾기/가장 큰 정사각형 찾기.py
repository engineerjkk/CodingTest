def solution(board):
    n=len(board)
    m=len(board[0])
    answer=board[0][0]
    for i in range(1,n):
        for j in range(1,m):
            if board[i][j]==1:
                board[i][j]=1+min(board[i-1][j-1],board[i-1][j],board[i][j-1])
                answer=max(answer,board[i][j])
    return answer**2