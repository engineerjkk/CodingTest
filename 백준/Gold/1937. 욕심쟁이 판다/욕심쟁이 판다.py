import sys 
sys.setrecursionlimit(10**6)  # 재귀 깊이 제한 늘리기
input = sys.stdin.readline 

n = int(input())
space = []
for _ in range(n):
    space.append(list(map(int, input().split())))

# dp[r][c]: (r,c)에서 시작했을 때 이동할 수 있는 최대 칸 수
dp = [[-1]*n for _ in range(n)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

def dfs(r, c):
    # 이미 계산된 값이 있다면 그 값을 반환
    if dp[r][c] != -1:
        return dp[r][c]
    
    # 현재 위치에서 시작하는 경우를 1로 초기화
    dp[r][c] = 1
    
    # 4방향 탐색
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        # 범위 안에 있고 다음 칸의 대나무가 더 많은 경우
        if in_range(nr, nc) and space[nr][nc] > space[r][c]:
            # 다음 칸에서의 최대 이동 칸 수 + 1과 현재 값 중 최댓값 선택
            dp[r][c] = max(dp[r][c], dfs(nr, nc) + 1)
    
    return dp[r][c]

# 모든 위치에서 시작해보기
answer = 0
for i in range(n):
    for j in range(n):
        answer = max(answer, dfs(i, j))

print(answer)