import sys 
input = sys.stdin.readline 
import heapq

n,m=map(int,input().split())
pq=list(map(int,input().split()))
heapq.heapify(pq)

for _ in range(m):
    a=heapq.heappop(pq)
    b=heapq.heappop(pq)
    c=a+b
    heapq.heappush(pq,c)
    heapq.heappush(pq,c)
print(sum(pq))