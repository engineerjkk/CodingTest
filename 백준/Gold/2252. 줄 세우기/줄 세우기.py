import sys
input = sys.stdin.readline
from collections import deque
n,m=map(int,input().split())
lst=[[] for _ in range(n)]
tmp=[0]*n

for _ in range(m):
    a,b=map(int,input().split())
    lst[a-1].append(b-1)
    tmp[b-1]+=1

queue=deque()
for i in range(n):
    if tmp[i]==0:
        queue.append(i)

answer=[]
while queue:
    u=queue.popleft()
    answer.append(u)
    for i in lst[u]:
        tmp[i]-=1
        if tmp[i]==0:
            queue.append(i)
for i in answer:
    print(i+1,end=" ")
