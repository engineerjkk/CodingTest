from collections import deque

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

def getNext(N, M, board, y, x, i):
    while True:
        nextY = y + dy[i]
        nextX = x + dx[i]
        if(0 <= nextY < N and 0 <= nextX < M and board[nextY][nextX] != 'D'):
            y = nextY
            x = nextX
        else: break
    return y, x

def sol(N, M, board, Y, X):
    visited = [[False] * M for _ in range(N)]
    q = deque([(Y, X)])
    visited[Y][X] = True
    answer = 0
    while q:
        s = len(q)
        for _ in range(s):
            y, x = q.popleft()
            if(board[y][x] == 'G'): return answer
            for i in range(4):
                nextY, nextX = getNext(N, M, board, y, x, i)
                if(visited[nextY][nextX] == False):
                    q.append((nextY, nextX))
                    visited[nextY][nextX] = True
        answer += 1
    return -1

def solution(board):
    answer = 0
    N = len(board)
    M = len(board[0])
    for i in range(N):
        for j in range(M):
            if(board[i][j] == 'R'):
                return sol(N, M, board, i, j)
