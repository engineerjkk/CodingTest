import sys
input = sys.stdin.readline
from collections import deque

n,m=map(int,input().split())
lst=[[] for _ in range(n)]
tmp=[0]*n
for i in range(m):
    a,b=map(int,input().split())
    lst[a-1].append(b-1)
    tmp[b-1]+=1

queue=deque()
for i in range(len(tmp)):
    if tmp[i]==0:
        queue.append(i)

answer=[]
while queue:
    q=queue.popleft()
    answer.append(q+1)
    for i in lst[q]:
        tmp[i]-=1
        if tmp[i]==0:
            queue.appendleft(i)

for i in answer:
    print(i,end=" ")