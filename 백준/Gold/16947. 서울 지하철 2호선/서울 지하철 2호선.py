import sys 
input = sys.stdin.readline 
from collections import deque 

n=int(input())
graph=[[] for _ in range(n)]

for _ in range(n):
    u,v=map(int,input().split())
    u-=1
    v-=1

    graph[u].append(v)
    graph[v].append(u)

degree=[]
for i in range(n):
    degree.append(len(graph[i]))

while True:
    leaf=[]
    for i in range(n):
        if degree[i]==1:
            leaf.append(i)
    
    if len(leaf)==0:
        break 

    for u in leaf:
        degree[u]=-1
        for v in graph[u]:
            if degree[v]!=-1:
                degree[v]-=1

visit=[False]*n
distance=[-1]*n
queue=deque()

for i in range(n):
    if degree[i] !=-1:
        queue.append(i)
        visit[i]=True
        distance[i]=0

while queue:
    u=queue.popleft()
    for v in graph[u]:
        if not visit[v]:
            queue.append(v)
            visit[v]=True 
            distance[v]=distance[u]+1
print(*distance)
    