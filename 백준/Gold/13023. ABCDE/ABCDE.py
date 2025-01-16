import sys 
input = sys.stdin.readline 

def dfs(graph,visit,u,depth,start):
    
    if depth==4:
        return True 
    
    for v in graph[u]:
        if visit[v]:
            continue 
        
        visit[v]=True 
        if dfs(graph,visit,v,depth+1,start):
            return True 
        visit[v]=False 
    return False 

def solution(n,m,edges):
    graph=[[] for _ in range(n)]
    for i in range(m):
        a,b=edges[i]
        graph[a].append(b)
        graph[b].append(a)
    
    for i in range(n):
        visit=[False]*n
        visit[i]=True 
        if dfs(graph,visit,i,0,i):
            return 1
    return 0
n,m=map(int,input().split())
edges=[]
for _ in range(m):
    edges.append(list(map(int,input().split())))

print(solution(n,m,edges))