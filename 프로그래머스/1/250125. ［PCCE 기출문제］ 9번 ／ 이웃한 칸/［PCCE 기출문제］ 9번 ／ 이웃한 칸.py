from collections import deque
dr=[-1,0,1,0]
dc=[0,1,0,-1]
def solution(board, h, w):
    answer = 0
    for i in range(4):
        nr=h+dr[i]
        nc=w+dc[i]
        if -1<nr<len(board) and -1<nc<len(board[0]):
            if board[h][w] == board[nr][nc]:
                answer+=1
    return answer