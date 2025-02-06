import heapq
import sys
input = sys.stdin.readline

def dijkstra(start, graph, N):
    distances = [float('inf')] * (N + 1)
    distances[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        curr_dist, curr = heapq.heappop(queue)
        
        if distances[curr] < curr_dist:
            continue
            
        for next_node, weight in graph[curr]:  # 여기만 수정
            distance = curr_dist + weight
            
            if distance < distances[next_node]:
                distances[next_node] = distance
                heapq.heappush(queue, (distance, next_node))
                
    return distances

def solution():
    N, M, X = map(int, input().split())
    
    # 리스트로 그래프 초기화
    graph = [[] for _ in range(N + 1)]
    reverse_graph = [[] for _ in range(N + 1)]
    
    # 리스트 방식으로 그래프 구성
    for _ in range(M):
        start, end, time = map(int, input().split())
        graph[start].append((end, time))
        reverse_graph[end].append((start, time))
    
    from_party = dijkstra(X, graph, N)
    to_party = dijkstra(X, reverse_graph, N)
    
    return max(from_party[i] + to_party[i] for i in range(1, N + 1))

print(solution())