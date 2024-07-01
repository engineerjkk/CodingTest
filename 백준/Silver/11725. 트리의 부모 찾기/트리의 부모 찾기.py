from collections import deque
import sys
input = sys.stdin.readline

n=int(input())
graph=[[] for _ in range(n+1)]
for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visited=[0]*(n+1)

queue=deque()
queue.append(1)
visited[1]=1
while queue:
    q=queue.popleft()
    for i in graph[q]:
        if visited[i]==0:
            queue.append(i)
            visited[i]=q
for i in visited[2:]:
    print(i)