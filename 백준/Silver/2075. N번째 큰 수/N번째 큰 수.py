import sys
input = sys.stdin.readline
import heapq

n=int(input())
space=[]
pq=[]
for _ in range(n):
    lst=list(map(int,input().split()))
    for i in lst:
        if len(pq)<n:
            heapq.heappush(pq,i)
        else:
            if pq[0]<i:
                heapq.heappush(pq,i)
                heapq.heappop(pq)
print(pq[0])

