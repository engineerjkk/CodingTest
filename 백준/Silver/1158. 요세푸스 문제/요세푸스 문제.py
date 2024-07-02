import sys
input = sys.stdin.readline
from collections import deque

n,k=map(int,input().split())
queue=deque()
for i in range(k,n+1):
    queue.append(i)
for i in range(1,k):
    queue.append(i)
answer=[]
while queue:
    answer.append(queue.popleft())
    queue.rotate(-(k-1))
ans=""
ans+="<"
for i in answer[:-1]:
    ans+=str(i)
    ans+=", "
ans+=str(answer[-1])
ans+=">"
print(ans)
