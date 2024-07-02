import sys
import heapq
input = sys.stdin.readline
n,m,x=map(int,input().split())
lst=[[] for _ in range(n)]
for _ in range(m):
    a,b,time=map(int,input().split())
    lst[a-1].append((b-1,time))
distance=[1e9]*(n)


def dijkstra_departure(start):
    queue=[]
    heapq.heappush(queue,(0,start))
    distance[start]=0
    while queue:
        dis,a=heapq.heappop(queue)
        if distance[a]<dis:
            continue
        for b,time in lst[a]:
            cost=dis+time
            if cost<distance[b]:
                distance[b]=cost
                heapq.heappush(queue,(cost,b))

def dijkstra_back(start):
    queue=[]
    heapq.heappush(queue,(0,start))
    distance2=[1e9]*(n)
    distance2[start]=0
    while queue:
        dis,a=heapq.heappop(queue)
        if distance2[a]<dis:
            continue
        for b,time in lst[a]:
            cost=dis+time
            if cost<distance2[b]:
                distance2[b]=cost
                heapq.heappush(queue,(cost,b))
    return distance2[x-1]

dijkstra_departure(x-1)
departure=distance[0]
back=[]
for i in range(n):
    back.append(dijkstra_back(i))

answer=[]
for i,j in zip(distance,back):
    answer.append(i+j)
print(max(answer))
