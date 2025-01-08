import sys
input = sys.stdin.readline

# 입력 받기
R, C, K = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]

# 상하좌우 이동
dx = [0, 0, -1, 1]  # 행 이동
dy = [-1, 1, 0, 0]  # 열 이동

answer = 0

def dfs(x, y, distance):
    global answer
    
    # 목적지(오른쪽 위)에 도달했고, 거리가 K와 같다면 카운트
    if x == 0 and y == C-1:
        if distance == K:
            answer += 1
        return
    
    # 현재 위치 방문 표시
    board[x][y] = 'v'
    
    # 네 방향으로 이동 시도
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        # 범위 체크 및 갈 수 있는 곳인지 확인
        if 0 <= nx < R and 0 <= ny < C and board[nx][ny] != 'T' and board[nx][ny] != 'v':
            dfs(nx, ny, distance + 1)
    
    # 백트래킹: 방문 표시 제거
    board[x][y] = '.'

# 시작점(왼쪽 아래)에서 DFS 시작
if board[R-1][0] != 'T':  # 시작점이 갈 수 있는 곳인지 확인
    dfs(R-1, 0, 1)

print(answer)