import sys 
input = sys.stdin.readline
from collections import deque 

a,k=map(int,input().split())

graph=[[] for _ in range(k+1)]

for i in range(1,k+1):
    if i+1<=k:
        graph[i].append(i+1)
    if 2*i<=k:
        graph[i].append(2*i)

visit=[False]*(k+1)
distance=[-1]*(k+1)
queue=deque() 

queue.append(a)
visit[a]=True 
distance[a]=0 

while queue:
    u=queue.popleft()
    for v in graph[u]:
        if not visit[v]:
            queue.append(v)
            visit[v]=True 
            distance[v]=distance[u]+1 

print(distance[k])
