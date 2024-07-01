import sys
input = sys.stdin.readline
from collections import deque
n,m=map(int,input().split())
lst=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    lst[a].append(b)
    lst[b].append(a)

def bfs(i):
    visit=[False]*(n+1)
    score=[0]*(n+1)
    queue=deque()
    queue.append(i)
    visit[i]=True
    while queue:
        q=queue.popleft()
        for j in lst[q]:
            if not visit[j]:
                queue.append(j)
                visit[j]=True
                score[j]=score[q]+1
    return sum(score)


dic={}
for i in range(1,n+1):
    ret=bfs(i)
    dic[i]=ret

print(sorted(dic.items(),key = lambda x:x[1])[0][0])