import sys
input = sys.stdin.readline
import heapq 

n,k=map(int,input().split())

diamonds=[]
for _ in range(n):
    m,v=map(int,input().split())
    diamonds.append((m,v))

bags=[]
for _ in range(k):
    bags.append(int(input()))

diamonds.sort()
bags.sort()

answer=0
pq=[]
idx=0

for bag in bags:
    while idx<n and diamonds[idx][0]<=bag:
        heapq.heappush(pq,-diamonds[idx][1])
        idx+=1
    
    if pq:
        answer-=heapq.heappop(pq)
print(answer)