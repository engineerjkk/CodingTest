import sys 
input = sys.stdin.readline 
from collections import deque 

s,t=map(int,input().split())

visit=set() 
queue=deque()
queue.append(s)
visit.add(s)
path={}
path[s]=''

while queue:
    u=queue.popleft()
    if u*u <=1e9 and u*u not in visit:
        queue.append(u*u)
        visit.add(u*u)
        path[u*u]=path[u]+'*'
    if u+u <=1e9 and u+u not in visit:
        queue.append(u+u)
        visit.add(u+u)
        path[u+u]=path[u]+'+'
    if u/u <=1e9 and u/u not in visit:
        queue.append(u/u)
        visit.add(u/u)
        path[u/u]=path[u]+'/'

if s==t:
    print(0)
elif t in path:
    print(path[t])
else:
    print(-1)