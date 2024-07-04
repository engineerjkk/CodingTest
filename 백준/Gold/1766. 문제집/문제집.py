import sys
input = sys.stdin.readline
import heapq
n,m=map(int,input().split())
lst=[[] for _ in range(n)]
tmp=[0]*n
for _ in range(m):
    a,b=map(int,input().split())
    lst[a-1].append(b-1)
    tmp[b-1]+=1

pq=[]
for i in range(n):
    if tmp[i]==0:
        heapq.heappush(pq,i)
answer=[]
while pq:
    q=heapq.heappop(pq)
    answer.append(q)
    for i in lst[q]:
        tmp[i]-=1
        if tmp[i]==0:
            heapq.heappush(pq,i)
for i in answer:
    print(i+1,end=" ")

