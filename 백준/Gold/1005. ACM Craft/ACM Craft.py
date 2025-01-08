import sys 
input = sys.stdin.readline 
from collections import deque 

t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    times=list(map(int,input().split()))
    graph=[[] for _ in range(n)]
    degree=[0]*n 
    dp=[0]*n 

    for _ in range(k):
        u,v=map(int,input().split())
        graph[u-1].append(v-1)
        degree[v-1]+=1 
    
    w=int(input())-1 

    queue=deque()
    for i in range(n):
        if degree[i]==0:
            queue.append(i)
            dp[i]=times[i]
    
    while queue:
        u=queue.popleft()
        for v in graph[u]:
            degree[v]-=1
            dp[v]=max(dp[v],dp[u]+times[v])
            if degree[v]==0:
                queue.append(v)
    
    print(dp[w])