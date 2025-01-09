import sys 
input = sys.stdin.readline 
from collections import deque 

n,k=map(int,input().split())
graph=[[] for _ in range(n)]

for _ in range(k):
    a,b=map(int,input().split())
    a-=1
    b-=1
    graph[a].append(b)

visit=[[False]*n for _ in range(n)]

for i in range(n):
    queue=deque()
    queue.append(i)
    visit[i][i]=True 

    while queue:
        u=queue.popleft()
        for v in graph[u]:
            if not visit[i][v]:
                queue.append(v)
                visit[i][v]=True 

s=int(input())
for _ in range(s):
    a,b=map(int,input().split())
    a-=1
    b-=1
    if visit[a][b]:
        print(-1)
    elif visit[b][a]:
        print(1)
    else:
        print(0)