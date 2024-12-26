import sys
input = sys.stdin.readline
import heapq

n,k,t=map(int,input().split())

lst=list(map(int,input().split()))
lst.sort()
pq=[]
idx=0
for _ in range(k):
    while idx<n and lst[idx]<t:
        heapq.heappush(pq,-lst[idx])
        idx+=1
    if len(pq)==0:
        break
    t+=(-heapq.heappop(pq))
print(t)
    