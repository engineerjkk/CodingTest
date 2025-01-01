import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
n=int(input())

graph=[[] for _ in range(n)]

for _ in range(n-1):
    u,v,w=map(int,input().split())
    u-=1
    v-=1
    graph[u].append((v,w))
    graph[v].append((u,w))

visit=[False]*n
distance=[0]*n

def dfs(u):
    visit[u]=True

    for v,w in graph[u]:
        if not visit[v]:
            distance[v]=distance[u]+w
            dfs(v)

dfs(0)

max_distance=0
who=0
for i in range(n):
    if max_distance<distance[i]:
        max_distance=distance[i]
        who=i

visit=[False]*n
distance=[0]*n
dfs(who)

max_distance=0
for i in range(n):
    if max_distance<distance[i]:
        max_distance=distance[i]

print(max_distance)