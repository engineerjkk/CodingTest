import sys
input = sys.stdin.readline
from collections import deque
n,m=map(int,input().split())
lst=[[] for _ in range(n)]
for _ in range(m):
    a,b=map(int,input().split())
    lst[a-1].append(b-1)
    lst[b-1].append(a-1)
visit=[False]*n

def bfs(i):
    queue=deque()
    queue.append(i)
    visit[i]=True

    while queue:
        q=queue.popleft()
        for j in lst[q]:
            if not visit[j]:
                visit[j]=True
                queue.append(j)

def dfs(i):
    stack=[i]
    visit[i]=True
    while stack:
        node=stack.pop()
        for j in lst[node]:
            if not visit[j]:
                visit[j]=True
                stack.append(j)

def dfs_recursive(i):
    visit[i]=True
    
    for j in lst[i]:
        if not visit[j]:
            dfs_recursive(j)

answer=0
for i in range(n):
    if visit[i]==False:
        dfs_recursive(i)
        answer+=1
print(answer)