import sys 
input = sys.stdin.readline 

t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    graph=[[] for _ in range(n)]

    for _ in range(m):
        u,v,w=map(int,input().split())
        u-=1
        v-=1
        graph[u].append((v,w))
        graph[v].append((u,w))
    
    visit=[False]*n
    dp=[0]*n 

    def dfs(u):
        visit[u]=True 
        is_leaf=True 
        for v,w in graph[u]:
            if not visit[v]:
                dfs(v)
                dp[u]+=min(w,dp[v])
                is_leaf=False 
        if u!=0 and is_leaf:
            dp[u]=1e9
    
    dfs(0)
    print(dp[0])