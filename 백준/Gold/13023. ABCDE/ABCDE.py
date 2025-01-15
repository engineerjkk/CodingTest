def dfs(graph, visited, current, depth, start):
    # 길이가 4인 경로를 찾았다면
    if depth == 4:
        return True
        
    # 현재 정점에서 연결된 모든 정점을 확인
    for next_vertex in graph[current]:
        # 이미 방문한 정점은 건너뛰기
        if visited[next_vertex]:
            continue
            
        # 다음 정점 방문
        visited[next_vertex] = True
        if dfs(graph, visited, next_vertex, depth + 1, start):
            return True
        visited[next_vertex] = False
        
    return False

def solution(N, M, edges):
    # 그래프 생성
    graph = [[] for _ in range(N)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
        
    # 각 정점을 시작점으로 하여 DFS 수행
    for start in range(N):
        visited = [False] * N
        visited[start] = True
        # 길이가 4인 경로를 찾았다면 1 반환
        if dfs(graph, visited, start, 0, start):
            return 1
            
    # 길이가 4인 경로를 찾지 못했다면 0 반환
    return 0

# 입력 처리
N, M = map(int, input().split())
edges = []
for _ in range(M):
    a, b = map(int, input().split())
    edges.append((a, b))

# 결과 출력
print(solution(N, M, edges))