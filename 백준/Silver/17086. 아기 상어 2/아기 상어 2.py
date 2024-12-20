from collections import deque

def find_max_safe_distance(grid, n, m):
    # 8방향 이동 (상하좌우 + 대각선)
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    
    # 상어 위치 찾기
    sharks = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                sharks.append((i, j))
    
    # BFS로 각 빈 칸의 안전 거리 계산
    def bfs():
        distances = [[-1] * m for _ in range(n)]
        queue = deque()
        
        # 상어 위치를 시작점으로 설정
        for shark in sharks:
            x, y = shark
            distances[x][y] = 0
            queue.append((x, y))
        
        while queue:
            x, y = queue.popleft()
            
            # 8방향 탐색
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                
                # 범위 체크 및 미방문 체크
                if 0 <= nx < n and 0 <= ny < m and distances[nx][ny] == -1:
                    distances[nx][ny] = distances[x][y] + 1
                    queue.append((nx, ny))
        
        return distances
    
    # 모든 칸의 안전 거리 계산
    distances = bfs()
    
    # 안전 거리의 최댓값 찾기
    max_distance = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:  # 빈 칸인 경우만 고려
                max_distance = max(max_distance, distances[i][j])
    
    return max_distance

# 입력 처리
n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

# 결과 출력
print(find_max_safe_distance(grid, n, m))