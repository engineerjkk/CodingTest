import sys 
input = sys.stdin.readline 

# 입력 받기
r, c = map(int, input().split())
board = []
for _ in range(r):
    board.append(list(input().strip()))

def in_range(x, y):
    return 0 <= x < r and 0 <= y < c

# 상하좌우 이동
dx = [-1, 1, 0, 0]  
dy = [0, 0, -1, 1]

answer = 1
visited = set()  # 방문한 알파벳을 저장

def dfs(x, y, count):
    global answer
    answer = max(answer, count)
    
    # 네 방향으로 이동 시도
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        # 범위 내에 있고, 해당 알파벳을 아직 방문하지 않았다면
        if in_range(nx, ny) and board[nx][ny] not in visited:
            visited.add(board[nx][ny])  # 알파벳 방문 처리
            dfs(nx, ny, count + 1)      # 다음 칸으로 이동
            visited.remove(board[nx][ny])  # 백트래킹

# 시작점의 알파벳을 방문 처리하고 DFS 시작
visited.add(board[0][0])
dfs(0, 0, 1)

print(answer)