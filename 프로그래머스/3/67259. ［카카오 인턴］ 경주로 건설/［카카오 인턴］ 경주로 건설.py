from collections import deque

def solution(board):
    N = len(board)
    # 방향: 상(0), 우(1), 하(2), 좌(3)
    # [dy, dx]
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    # 비용 배열: [y좌표][x좌표][진입방향]
    cost = [[[float('inf')] * 4 for _ in range(N)] for _ in range(N)]
    
    def is_valid(y, x):
        return 0 <= y < N and 0 <= x < N and board[y][x] == 0
    
    def bfs():
        # Queue: (y좌표, x좌표, 방향, 비용)
        queue = deque()
        # 시작점에서 오른쪽과 아래로 이동할 수 있음
        queue.append((0, 0, 1, 0))  # 오른쪽
        queue.append((0, 0, 2, 0))  # 아래
        
        # 시작점의 비용 초기화
        for i in range(4):
            cost[0][0][i] = 0
            
        while queue:
            y, x, direction, current_cost = queue.popleft()
            
            # 현재 비용이 이미 알고 있는 최소 비용보다 크면 스킵
            if current_cost > cost[y][x][direction]:
                continue
                
            # 모든 방향으로 이동
            for new_direction in range(4):
                # 반대 방향으로는 이동할 수 없음
                if abs(new_direction - direction) == 2:
                    continue
                    
                new_y = y + directions[new_direction][0]
                new_x = x + directions[new_direction][1]
                
                if not is_valid(new_y, new_x):
                    continue
                    
                # 새로운 비용 계산
                new_cost = current_cost + 100
                if new_direction != direction:
                    new_cost += 500
                    
                # 더 적은 비용으로 도달할 수 있다면 갱신
                if new_cost < cost[new_y][new_x][new_direction]:
                    cost[new_y][new_x][new_direction] = new_cost
                    queue.append((new_y, new_x, new_direction, new_cost))
    
    bfs()
    
    # 도착점에서의 최소 비용 반환
    return min(cost[N-1][N-1])