import sys 
input = sys.stdin.readline 
from collections import deque 

n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
for _ in range(n-1):
    u,v,w=map(int,input().split())
    graph[u].append((v,w))
    graph[v].append((u,w))
answer=[]
for _ in range(m):
    a,b=map(int,input().split())
    queue=deque()
    queue.append((a,0))
    visit=[False]*(n+1)
    visit[a]=True
    while queue:
        now,dis=queue.popleft()
        if now==b:
            break 
        for v,w in graph[now]:
            if not visit[v]:
                visit[v]=True 
                queue.append((v,dis+w))
    answer.append(dis)
for i in range(len(answer)):
    print(answer[i])