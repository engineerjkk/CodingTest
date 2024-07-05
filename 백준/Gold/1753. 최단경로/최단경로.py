import sys
import heapq
input=sys.stdin.readline
V,E=map(int,input().split())
K=int(input())
lst=[[] for _ in range(V+1)]
for _ in range(E):
    u,v,w=map(int,input().split())
    lst[u].append((v,w))

distance=[1e9]*(V+1)

def dijkstra(start):
    pq=[]
    heapq.heappush(pq,(0,start))
    distance[start]=0
    while pq:
        dis,now=heapq.heappop(pq)
        if distance[now]<dis:
            continue
        for v,w in lst[now]:
            cost=dis+w
            if cost<distance[v]:
                distance[v]=cost
                heapq.heappush(pq,(cost,v))


dijkstra(K)

for i in range(1,V+1):
    if distance[i]==1e9:
        print("INF")
    else:
        print(distance[i])
    