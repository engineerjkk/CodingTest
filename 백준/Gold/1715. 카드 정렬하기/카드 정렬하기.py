import sys
input = sys.stdin.readline
import heapq
n=int(input())
lst=[]
for _ in range(n):
    heapq.heappush(lst,int(input()))

ans=0
while len(lst)>1:
    a=heapq.heappop(lst)
    b=heapq.heappop(lst)
    c=a+b
    heapq.heappush(lst,c)
    ans+=a
    ans+=b
print(ans)