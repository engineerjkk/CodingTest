import sys 
input = sys.stdin.readline 
sys.setrecursionlimit(10**8)

N,R,Q=map(int,input().split())
R-=1

graph=[[] for _ in range(N)]
for _ in range(N-1):
    u,v=map(int,input().split())
    u-=1
    v-=1
    graph[u].append(v)
    graph[v].append(u)

visit=[False]*N
dp=[0]*N
def dfs(u):
    visit[u]=True 
    dp[u]=1 

    for v in graph[u]:
        if not visit[v]:
            dfs(v)
            dp[u]+=dp[v]

dfs(R)

for _ in range(Q):
    u=int(input())
    u-=1
    print(dp[u])
