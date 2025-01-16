import sys 
input = sys.stdin.readline 
sys.setrecursionlimit(10**6)

n=int(input())
graph=[[] for _ in range(n)]

for _ in range(n-1):
    a,b=map(int,input().split())
    a-=1
    b-=1
    graph[a].append(b)
    graph[b].append(a)

visit=[False]*n 
sizes=[0]*n 

def dfs(u):
    visit[u]=True 
    sizes[u]=1 

    for v in graph[u]:
        if not visit[v]:
            dfs(v)
            sizes[u]+=sizes[v]

dfs(0)
answer=0
for i in range(1,n):
    answer+=sizes[i]*(sizes[i]-1)//2
    answer+=sizes[i]*(n-sizes[i])
print(answer)
