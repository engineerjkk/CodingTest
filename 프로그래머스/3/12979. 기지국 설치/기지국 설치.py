def solution(n, stations, w):
    answer = 0
    # 그리디하게 해결해봅니다.
    # i가 커버가 안되면 i+w에 기지국을 세우고 i+2w + 1로 이동해서 반복합니다.
    # 이를 위해서 i가 커버가 되냐 안되냐를 빠르게 파악해야 합니다.
    # 계산 편의를 위해 기지국 위치를 0-based로 바꿉니다.
    stations = [s-1 for s in stations]
    stations.sort()
    
    # 이제 투 포인터로 해결합니다.
    i, j = 0, 0
    
    while i < n and j < len(stations):
        if i < stations[j] - w:
            answer += 1
            i = i + 2*w + 1
            
        if stations[j] - w <= i <= stations[j] + w:
            i = stations[j] + w + 1
        
        if i > stations[j] + w:
        	j += 1
    
    while i < n:
        answer += 1
        i = i + 2*w + 1
            
    return answer