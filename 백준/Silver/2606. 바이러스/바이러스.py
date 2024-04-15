from collections import deque
import sys
input = sys.stdin.readline

n=int(input())
m=int(input())
network=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    network[a].append(b)
    network[b].append(a)
queue=deque()
queue.append(1)
cnt=0
visited=[False]*(n+1)
visited[1]=True
while queue:
    virus=queue.popleft()
    for i in network[virus]:
        if not visited[i]:
            visited[i]=True
            queue.append(i)
            cnt+=1
print(cnt)