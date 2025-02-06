import sys 
input = sys.stdin.readline 
import heapq 

n,m,x=map(int,input().split())
graph=[[] for _ in range(n+1)]
reverse_graph=[[] for _ in range(n+1)]

for _ in range(m):
    start,end,time=map(int,input().split())
    graph[start].append((end,time))
    reverse_graph[end].append((start,time))

def dijkstra(start,graph,n):
    distances=[1e9]*(n+1)
    distances[start]=0
    pq=[]
    heapq.heappush(pq,(0,start))
    while pq:
        curr_dist,curr=heapq.heappop(pq)
        if distances[curr]<curr_dist:
            continue
        for next_node,weight in graph[curr]:
            distance=curr_dist+weight
            if distance<distances[next_node]:
                distances[next_node]=distance 
                heapq.heappush(pq,(distance,next_node))
    return distances

to_party=dijkstra(x,graph,n)
to_home=dijkstra(x,reverse_graph,n)

max_time=0
for i in range(1,n+1):
    max_time=max(max_time,to_party[i]+to_home[i])
print(max_time)