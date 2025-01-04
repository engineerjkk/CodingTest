import sys 
input = sys.stdin.readline 
from collections import deque 

n=int(input())
m=int(input())
graph=[[] for _ in range(n)]
count=[0]*n 

for _ in range(m):
    x,y,k=map(int,input().split())
    x-=1
    y-=1

    graph[x].append((y,k))
    count[y]+=1

answer=[0]*n 
answer[n-1]=1

queue=deque()
for i in range(n):
    if count[i]==0:
        queue.append(i)

while len(queue)!=0:
    u=queue.popleft()
    for v,w in graph[u]:
        answer[v]+=w*answer[u]
        count[v]-=1 
        if count[v]==0:
            queue.append(v)

for i in range(n):
    if len(graph[i])==0:
        print(i+1,answer[i])