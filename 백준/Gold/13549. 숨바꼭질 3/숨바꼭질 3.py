import sys
input = sys.stdin.readline
from collections import deque

n,k=map(int,input().split())

visit=[-1]*100001

queue=deque()
queue.append(n)
visit[n]=0

while queue:
    r=queue.popleft()

    if r==k:
        print(visit[r])
        exit()
    if 0<=2*r<=100000 and visit[2*r]==-1:
        queue.appendleft(2*r)
        visit[2*r]=visit[r]
    
    for nr in (r-1,r+1):
        if 0<=nr<=100000 and visit[nr]==-1:
            queue.append(nr)
            visit[nr]=visit[r]+1
print(-1)