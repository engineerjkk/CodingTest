import sys 
input = sys.stdin.readline 

n,m=map(int,input().split())
graph=[[] for _ in range(n)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph,visit,u,depth):
    if depth==4:
        return True 
    for v in graph[u]:
        if visit[v]:
            continue 
        visit[v]=True 
        if dfs(graph,visit,v,depth+1):
            return True 
        visit[v]=False
    return False

for i in range(n):
    visit=[False]*n
    visit[i]=True 
    if dfs(graph,visit,i,0):
        print(1)
        exit()
print(0)