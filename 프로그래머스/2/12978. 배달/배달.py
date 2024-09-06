from collections import deque
def solution(N, road, K):
    graph=[[] for _ in range(N+1)]
    for a,b,c in road:
        graph[a].append((b,c))
        graph[b].append((a,c))
    visit=[1e9]*(N+1)
    def dijkstra(start):
        queue=deque()
        queue.append((start,0))
        visit[start]=0
        while queue:
            now,dis=queue.popleft()
            for v,w in graph[now]:
                cost=dis+w
                if cost<visit[v]:
                    visit[v]=cost
                    queue.append((v,cost))
    dijkstra(1)
    answer=0
    for i in range(1,N+1):
        if visit[i]<=K:
            answer+=1
    return answer