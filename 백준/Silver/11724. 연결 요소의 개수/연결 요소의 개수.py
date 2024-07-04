import sys
input = sys.stdin.readline
from collections import deque
n,m = map(int,input().split())
lst=[[] for _ in range(n)]
for _ in range(m):
    a,b=map(int,input().split())
    lst[a-1].append(b-1)
    lst[b-1].append(a-1)

visit=[False]*n

def bfs(start):
    queue=deque()
    queue.append(start)
    visit[start]=True
    while queue:
        q=queue.popleft()
        for i in lst[q]:
            if not visit[i]:
                visit[i]=True
                queue.append(i)
cnt=0
for i in range(n):
    if visit[i]==False:
        bfs(i)
        cnt+=1
print(cnt)