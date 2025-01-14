import sys 
input = sys.stdin.readline 
from collections import deque 

def in_range(r, c):
    return 0 <= r < n and 0 <= c < m 

def bfs(i, j, height, visit):
    queue = deque([(i, j)])
    visit[i][j] = True
    count = 1  # 물이 고일 수 있는 칸의 수
    flag = True  # 수영장이 될 수 있는지 체크
    
    while queue:
        r, c = queue.popleft()
        
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            
            # 경계를 벗어나는 경우
            if not in_range(nr, nc):
                flag = False
                continue
            
            # 현재 수위보다 낮거나 같고 아직 방문하지 않은 칸
            if space[nr][nc] <= height and not visit[nr][nc]:
                visit[nr][nc] = True
                queue.append((nr, nc))
                count += 1
    
    # 수영장이 될 수 있는 경우에만 칸 수 반환
    return count if flag else 0

# 입력 받기
n, m = map(int, input().split())
space = []
for _ in range(n):
    space.append(list(map(int, input().strip())))

# 방향 벡터
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 높이를 1부터 8까지 올리면서 확인
answer = 0
for height in range(1, 9):
    visit = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            # 현재 수위보다 낮고 아직 체크하지 않은 곳
            if space[i][j] <= height and not visit[i][j]:
                answer += bfs(i, j, height, visit)

print(answer)