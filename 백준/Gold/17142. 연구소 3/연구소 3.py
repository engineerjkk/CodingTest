import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N, M = map(int, input().split())
lab = []
virus = []
total_empty = 0

for _ in range(N):
    lab.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if lab[i][j] == 2:
            virus.append([i, j])

        elif lab[i][j] == 0:
            total_empty += 1

def bfs(board, virus_list, remain):
    global min_time
    visited = [[False for _ in range(N)] for _ in range(N)]
    queue = deque()
    for v in virus_list:
        i, j = v
        visited[i][j] = True
        queue.append([i, j, 0])

    while queue:
        x, y, time = queue.popleft()

        if time >= min_time:
            return 1e9

        if board[x][y] == 0:
            remain -= 1

        if remain == 0:
            return time

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny] != 1:
                    if not visited[nx][ny]:
                        visited[nx][ny] = True
                        queue.append([nx, ny, time + 1])
    return 1e9

def combinations(lst,r):
    def generate_combinations(lst,start,r,result,results):
        if r==0:
            results.append(result[:])
            return
        for i in range(start,len(lst)):
            result.append(lst[i])
            generate_combinations(lst,i+1,r-1,result,results)
            result.pop()
    results=[]
    generate_combinations(lst,0,r,[],results)
    return results
    

min_time = 1e9
for c in combinations(virus, M):
    min_time = min(min_time, bfs(lab, c, total_empty))

if min_time == 1e9:
    min_time = -1
print(min_time)