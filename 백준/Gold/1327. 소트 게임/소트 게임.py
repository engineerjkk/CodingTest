import sys 
input = sys.stdin.readline 
from collections import deque 

n,k=map(int,input().split())
sequence=tuple(map(int,input().split()))
visit=set() 
queue=deque()
queue.append((sequence,0))

flag=False
while queue:
    seq,times=queue.popleft() 

    if seq==tuple(range(1,n+1)):
        flag=True
        break

    for i in range(n-k+1):
        next_seq=seq[:i]+seq[i:i+k][::-1]+seq[i+k:]
        if next_seq not in visit:
            visit.add(next_seq)
            queue.append((next_seq,times+1))

if flag:
    print(times)
else:
    print(-1)