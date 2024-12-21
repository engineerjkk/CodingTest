import sys
input = sys.stdin.readline
import heapq

n=int(input())
courses=[]
for _ in range(n):
    start,end=map(int,input().split())
    courses.append((start,end))

courses.sort()
pq=[]
heapq.heappush(pq,courses[0][1])
room=1
for i in range(1,n):
    earliest=pq[0]
    if earliest<=courses[i][0]:
        heapq.heappop(pq)
    else:
        room+=1
    heapq.heappush(pq,courses[i][1])
print(room)