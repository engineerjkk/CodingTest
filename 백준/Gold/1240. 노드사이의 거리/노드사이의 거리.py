from collections import deque

n,m=map(int,input().split())
lst=[[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,d=map(int,input().split())
    lst[a].append((b,d))
    lst[b].append((a,d))
answer=[]
for _ in range(m):
    a,b=map(int,input().split())
    visit=[False]*(n+1)
    dis=0
    queue=deque()
    queue.append((a,0))
    visit[a]=True
    while queue:
        r,distance=queue.popleft()
        if r==b:
            break
        for n_a,distance2 in lst[r]:
            if not visit[n_a]:
                visit[n_a]=True
                queue.append((n_a,distance+distance2))
    answer.append(distance)
for i in answer:
    print(i)