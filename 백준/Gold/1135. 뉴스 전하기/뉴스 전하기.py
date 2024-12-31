import sys
input = sys.stdin.readline

n=int(input())
par=list(map(int,input().split()))

child=[[] for _ in range(n)]
for i in range(1,n):
    child[par[i]].append(i)

d=[0]*n
def dfs(u):
    times=[]
    for v in child[u]:
        dfs(v)
        times.append(d[v])
    times.sort(reverse=True)
    d[u]=0
    for i in range(len(times)):
        d[u]=max(d[u],i+1+times[i])

dfs(0)
print(d[0])