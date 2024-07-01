import sys
input = sys.stdin.readline
n=int(input())
m=int(input())
lst=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    lst[a].append(b)
    lst[b].append(a)

cnt=0
def dfs(node):
    global cnt
    visit[node]=True
    for i in lst[node]:
        if not visit[i]:
            cnt+=1
            dfs(i)
    return cnt
visit=[False]*(n+1)
node=1
visit[node]=True
print(dfs(node))