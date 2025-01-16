import sys 
input = sys.stdin.readline 
from collections import deque 

n,k=map(int,input().split())
sequence=tuple(map(int,input().split()))
queue=deque()
queue.append((sequence,0))
visit=set()

flag=False
while queue:
    current,times=queue.popleft()

    if current==tuple(range(1,n+1)):
        flag=True 
        break 

    for i in range(n-k+1):
        next_sequence=current[:i]+current[i:i+k][::-1]+current[i+k:]
        if next_sequence not in visit:
            visit.add(next_sequence)
            queue.append((next_sequence,times+1))
if flag:
    print(times)
else:
    print(-1)
