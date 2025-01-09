import sys 
input = sys.stdin.readline 
from collections import deque 

n=int(input())
friends=[]
for _ in range(n):
    friends.append(list(map(str,input().strip())))

max_count=0
for i in range(n):
    queue=deque()
    queue.append(i)
    visit=[False]*n
    visit[i]=True 
    distance=[-1]*n
    distance[i]=0

    while queue:
        u=queue.popleft()
        for v in range(n):
            if friends[u][v]=='Y' and not visit[v]:
                queue.append(v)
                visit[v]=True 
                distance[v]=distance[u]+1 
    count=0
    for j in range(n):
        if i!=j and distance[j]!=-1 and distance[j]<=2:
            count+=1
    max_count=max(max_count,count)
print(max_count)