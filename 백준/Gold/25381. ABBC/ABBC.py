import sys 
input = sys.stdin.readline 
from collections import deque 
s=input().strip() 
n=len(s)

queue=deque()
for i in range(n):
    if s[i]=='B':
        queue.append(i)

answer=0
for i in range(n):
    if s[i]=='C':
        if queue and queue[0]<i:
            queue.popleft()
            answer+=1 

for i in range(n-1,-1,-1):
    if s[i]=='A':
        if queue and queue[-1]>i:
            queue.pop()
            answer+=1
print(answer)