import sys
import heapq
input = sys.stdin.readline
V,E=map(int,input().split())
K=int(input())

graph=[[] for _ in range(V+1)]
for _ in range(E):
    u,v,w=map(int,input().split())
    graph[u].append((v,w))

distance=[1e9]*(V+1)

def dijkstra(start):
    queue=[]
    heapq.heappush(queue,(0,start))
    distance[start]=0

    while queue:
        dis,now=heapq.heappop(queue)
        if distance[now]<dis:
            continue
        for v,w in graph[now]:
            cost=dis+w
            if cost<distance[v]:
                distance[v]=cost
                heapq.heappush(queue,(cost,v))


dijkstra(K)

for num in range(1,V+1):
    if distance[num]==1e9:
        print("INF")
    else:
        print(distance[num])