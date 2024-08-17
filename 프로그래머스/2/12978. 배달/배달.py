import heapq
def solution(N, road, K):
    answer = 0
    graph=[[] for _ in range(N+1)]
    for u,v,w in road:
        graph[u].append((v,w))
        graph[v].append((u,w))
    distance=[1e9]*(N+1)
    def dijkstra(start):
        pq=[]
        heapq.heappush(pq,(0,start))
        distance[start]=0
        while pq:
            dis,now=heapq.heappop(pq)
            if distance[now]<dis:
                continue
            for v,w in graph[now]:
                cost=dis+w
                if cost<distance[v]:
                    distance[v]=cost
                    heapq.heappush(pq,(cost,v))
    dijkstra(1)
    for i in range(1,N+1):
        if distance[i]<=K:
            answer+=1
                    
    return answer