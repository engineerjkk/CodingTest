import sys
input = sys.stdin.readline
n=int(input())
lst=[[] for _ in range(n+1)]
for _ in range(n-1):
    a,b=map(int,input().split())
    lst[a].append(b)
    lst[b].append(a)

def dfs(i):
    visit[i]=True
    stack=[i]
    while stack:
        node=stack.pop()
        for j in lst[node]:
            if visit[j]==False:
                visit[j]=True
                stack.append(j)
                answer[j]=node

answer=[0]*(n+1)
visit=[False]*(n+1)
root=1
dfs(root)
for i in range(2,n+1):
    print(answer[i])

