def solution(N, L, signals):
    current_time = 0  # 현재 시간
    current_position = 0  # 현재 위치
    
    for signal in signals:
        position, red_time, green_time = signal
        
        # 다음 신호등까지 이동
        move_time = position - current_position
        current_time += move_time
        current_position = position
        
        # 현재 시간에서 신호등의 상태 확인
        cycle_time = red_time + green_time
        time_in_cycle = current_time % cycle_time
        
        # 빨간불이면 기다려야 함
        if time_in_cycle < red_time:
            wait_time = red_time - time_in_cycle
            current_time += wait_time
    
    # 마지막 신호등부터 도착지점까지 이동
    current_time += L - current_position
    
    return current_time

# 입력 처리
N, L = map(int, input().split())
signals = []
for _ in range(N):
    D, R, G = map(int, input().split())
    signals.append((D, R, G))

# 결과 출력
print(solution(N, L, signals))