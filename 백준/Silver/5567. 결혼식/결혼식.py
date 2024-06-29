import sys
input = sys.stdin.readline
from collections import deque
n=int(input())
m=int(input())
lst=[[] for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    lst[a].append(b)
    lst[b].append(a)

queue=deque()
queue.append(1)
first=lst[1]
total=[]
if first:
    for i in first:
        for j in lst[i]:
            total.append(j)
answer=list(set(first+total))
if 1 in answer:
    answer.remove(1)
print(len(answer))
