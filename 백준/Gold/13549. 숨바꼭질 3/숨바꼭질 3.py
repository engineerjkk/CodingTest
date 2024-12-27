import sys
input= sys.stdin.readline
from collections import deque

n,k=map(int,input().split())
MAX=100000
visit=[-1]*(MAX+1)

visit[n]=0
queue=deque()
queue.append(n)
while queue:
    r=queue.popleft()

    if r==k:
        print(visit[r])
        exit()
    
    if 0<=2*r<=MAX and visit[2*r]==-1:
        queue.appendleft(2*r)
        visit[2*r]=visit[r]
    
    for nr in (r-1,r+1):
        if 0<=nr<=MAX and visit[nr]==-1:
            queue.append(nr)
            visit[nr]=visit[r]+1
print(-1)