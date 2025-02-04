from collections import deque


def solution(board):
    N = len(board)
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    
    cost = [[[1e9] * 4 for _ in range(N)] for _ in range(N)]
    for i in range(4):
        cost[0][0][i] = 0
    
    queue = deque()
    # 시작점에서는 오른쪽(1)과 아래(2)로만 이동 가능
    queue.append((0, 0, 1, 0))
    queue.append((0, 0, 2, 0))

    def in_range(r,c):
        return -1<r<N and -1<c<N
    
    while queue:
        r, c, d, curr_cost = queue.popleft()
        
        # 더 큰 비용이면 스킵
        if curr_cost > cost[r][c][d]:
            continue
            
        # 4방향 탐색
        for nd in range(4):
            # 왔던 방향으로는 되돌아가지 않음
            if abs(nd - d) == 2:
                continue
                
            nr = r + dr[nd]
            nc = c + dc[nd]
            
            # 범위 체크와 벽이 아닌지 확인
            if in_range(nr,nc) and board[nr][nc] == 0:
                # 비용 계산 (직선 100원, 코너 500원 추가)
                new_cost = curr_cost + 100 + (500 if nd != d else 0)

                # 최소 비용 갱신
                if new_cost < cost[nr][nc][nd]:
                    cost[nr][nc][nd] = new_cost
                    queue.append((nr, nc, nd, new_cost))

    # 도착점의 모든 방향 중 최소 비용 반환
    return min(cost[N-1][N-1])