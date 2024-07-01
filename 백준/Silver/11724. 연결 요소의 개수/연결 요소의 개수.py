import sys
input = sys.stdin.readline
from collections import deque
n,m=map(int,input().split())
lst=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    lst[a].append(b)
    lst[b].append(a)

visit=[False]*(n+1)

def bfs(i):
    queue=deque()
    queue.append(i)
    visit[i]=True
    while queue:
        q=queue.popleft()
        for j in lst[q]:
            if not visit[j]:
                queue.append(j)
                visit[j]=True
    return True


cnt=0
for i in range(1,n+1):
    if visit[i]==False:
        bfs(i)
        cnt+=1
print(cnt)


