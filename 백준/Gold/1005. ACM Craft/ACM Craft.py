import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    time = list(map(int, input().split()))  # 각 건물당 건설에 걸리는 시간
    graph = [[] for _ in range(N)]  # 그래프
    indegree = [0] * N  # 진입 차수
    dp = [0] * N  # 해당 건물까지 걸리는 최대 시간
    
    # 그래프 생성 및 진입 차수 계산
    for _ in range(K):
        X, Y = map(int, input().split())
        graph[X-1].append(Y-1)
        indegree[Y-1] += 1
    
    W = int(input()) - 1  # 목표 건물
    
    # 위상 정렬 시작
    q = deque()
    
    # 진입 차수가 0인 노드 큐에 삽입 및 초기 시간 설정
    for i in range(N):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = time[i]
    
    # 위상 정렬 수행
    while q:
        cur = q.popleft()
        
        # 현재 건물에서 지을 수 있는 다음 건물들 확인
        for next_building in graph[cur]:
            indegree[next_building] -= 1
            # 다음 건물의 최대 소요시간 갱신
            dp[next_building] = max(dp[next_building], dp[cur] + time[next_building])
            
            # 진입 차수가 0이 된 건물 큐에 삽입
            if indegree[next_building] == 0:
                q.append(next_building)
    
    print(dp[W])