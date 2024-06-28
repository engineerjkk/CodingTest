import sys
input = sys.stdin.readline
from collections import deque
n,k=map(int,input().split())
lst=list(map(int,input().split()))
MAX=0

psum=[0]
value=0
for i in range(n):
    value+=lst[i]
    psum.append(value)

length=2
left=0
right=k
ans=-sys.maxsize
while right<n+1:
    value=psum[right]-psum[left]
    ans=max(ans,value)
    left+=1
    right+=1

print(ans)
    