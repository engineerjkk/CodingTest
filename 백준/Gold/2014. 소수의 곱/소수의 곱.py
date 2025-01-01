import sys
input = sys.stdin.readline
import heapq

k,n=map(int,input().split())
lst=list(map(int,input().split()))

pq=[]
for i in lst:
    heapq.heappush(pq,i)

v=0
for _ in range(n):
    v=heapq.heappop(pq)
    
    for p in lst:
        if v*p>=2**31:
            break
        heapq.heappush(pq,v*p)
        if v%p==0:
            break
print(v)