import sys 
input = sys.stdin.readline 
from collections import deque 

a,k=map(int,input().split())

graph=[[] for _ in range(k+1)]

for i in range(1,k+1):
    if i+1<=k:
        graph[i].append(i+1)
    if i*2<=k:
        graph[i].append(i*2)

queue=deque()
queue.append(a)
visit=[False]*(k+1)
visit[a]=True 
step=[-1]*(k+1)
step[a]=0
while queue:
    u=queue.popleft()
    for v in graph[u]:
        if not visit[v]:
            visit[v]=True 
            queue.append(v) 
            step[v]=step[u]+1
print(step[k])