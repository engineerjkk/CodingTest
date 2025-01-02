import sys
input = sys.stdin.readline
from collections import deque
import heapq

n,m,k=map(int,input().split())
initial_k=k
lst=list(map(int,input().split()))
friends=[]
for i in range(n):
    friends.append((lst[i],i))

friends.sort()

graph=[[] for _ in range(n)]
for _ in range(m):
    v,w=map(int,input().split())
    v-=1
    w-=1
    graph[v].append(w)
    graph[w].append(v)

queue=deque()
visit=[False]*n

flag=True
for f,i in (friends):
    if not visit[i]:
        visit[i]=True
        queue.append(i)
        k-=f
        if k<0:
            flag=False
            break
        while queue:
            r=queue.popleft()
            for v in graph[r]:
                if not visit[v]:
                    visit[v]=True
                    queue.append(v)


for i in range(n):
    if visit[i]==False :
        flag=False

if flag and k>=0:
    print(initial_k-k)
else:
    print("Oh no")
    


