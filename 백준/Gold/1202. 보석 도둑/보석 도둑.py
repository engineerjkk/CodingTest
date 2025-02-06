import sys 
input = sys.stdin.readline 
import heapq 

n,k=map(int,input().split())
diamonds=[]
for _ in range(n):
    diamonds.append(list(map(int,input().split())))

bags=[]
for _ in range(k):
    bags.append(int(input()))

diamonds.sort()
bags.sort()

pq=[]
idx=0
answer=0
for bag in bags:
    while idx<n and diamonds[idx][0]<=bag:
        heapq.heappush(pq,-diamonds[idx][1])
        idx+=1 
    if pq:
        answer-=heapq.heappop(pq)
print(answer)