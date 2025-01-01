import sys
input = sys.stdin.readline
import heapq

n=int(input())
due=[[] for _ in range(1001)]

for _ in range(n):
    d,w=map(int,input().split())
    due[d].append(w)

pq=[]
answer=0
for i in range(1000,0,-1):
    
    for w in due[i]:
        heapq.heappush(pq,-w)
    
    if len(pq)>0:
        answer-=heapq.heappop(pq)
print(answer)