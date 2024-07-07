import sys
input = sys.stdin.readline
import heapq
n,m=map(int,input().split())
adj=[[] for _ in range(n)]

need_to_learn=[0]*n
for _ in range(m):
    a,b=map(int,input().split())
    adj[a-1].append(b-1)
    need_to_learn[b-1]+=1

pq=[]
for i in range(n):
    if need_to_learn[i]==0:
        heapq.heappush(pq,i)

learn=[]
while pq:
    u=heapq.heappop(pq)
    learn.append(u)
    for v in adj[u]:
        need_to_learn[v]-=1
        if need_to_learn[v]==0:
            heapq.heappush(pq,v)

for i in range(n):
    print(learn[i]+1,end=" ")